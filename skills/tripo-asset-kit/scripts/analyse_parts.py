import bpy, bmesh, sys, json, math
from mathutils import Vector

args = sys.argv[sys.argv.index('--') + 1:]
src, out_prefix = args[0], args[1]

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=src)

report = {'parts': [], 'images': []}
for img in bpy.data.images:
    report['images'].append({'name': img.name, 'size': list(img.size)})

for ob in [o for o in bpy.context.scene.objects if o.type == 'MESH']:
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    tris_before = sum(len(f.verts) - 2 for f in bm.faces)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bm.edges.ensure_lookup_table()
    holes = sum(1 for e in bm.edges if e.is_boundary)
    seen, comps = set(), 0
    for v in bm.verts:
        if v.index in seen:
            continue
        comps += 1
        stack = [v]
        while stack:
            w = stack.pop()
            if w.index in seen:
                continue
            seen.add(w.index)
            stack.extend(e.other_vert(w) for e in w.link_edges if e.other_vert(w).index not in seen)
    uv = ob.data.uv_layers.active
    mats = [m.name for m in ob.data.materials if m]
    dims = [round(d, 3) for d in ob.dimensions]
    report['parts'].append({'name': ob.name, 'tris': tris_before, 'welded_components': comps,
                            'boundary_edges_after_weld': holes, 'dims': dims, 'materials': mats,
                            'uv': uv.name if uv else None})
    bm.free()

json.dump(report, open(out_prefix + '.parts.json', 'w'), indent=1)

# textured three-quarter render (Workbench, texture colours)
scene = bpy.context.scene
scene.render.engine = 'BLENDER_WORKBENCH'
scene.display.shading.light = 'STUDIO'
scene.display.shading.color_type = 'TEXTURE'
scene.render.resolution_x = scene.render.resolution_y = 1100
scene.render.film_transparent = False
world = bpy.data.worlds.new('w'); scene.world = world
mins = Vector((1e9,) * 3); maxs = Vector((-1e9,) * 3)
for ob in scene.objects:
    if ob.type == 'MESH':
        for c in ob.bound_box:
            p = ob.matrix_world @ Vector(c)
            mins = Vector(map(min, mins, p)); maxs = Vector(map(max, maxs, p))
center = (mins + maxs) / 2
size = max(maxs - mins)
cam_data = bpy.data.cameras.new('cam'); cam_data.type = 'ORTHO'; cam_data.ortho_scale = size * 1.25
cam = bpy.data.objects.new('cam', cam_data); scene.collection.objects.link(cam); scene.camera = cam
for name, az, el in (('tq', 35, 30), ('back', 215, 30)):
    a, e = math.radians(az), math.radians(el)
    d = Vector((math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e)))
    cam.location = center + d * size * 3
    cam.rotation_euler = (center - cam.location).to_track_quat('-Z', 'Y').to_euler()
    scene.render.filepath = out_prefix + '.textured.' + name + '.png'
    bpy.ops.render.render(write_still=True)
print('ANALYSE_PARTS_OK')
