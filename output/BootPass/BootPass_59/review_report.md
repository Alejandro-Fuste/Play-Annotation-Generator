# Play-Annotation-Generator Annotation Review — BootPass_59

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_59`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 48
- **Ball Tracks:** 0
- **Action Segments:** 138
- **Validation Warnings:** 212
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 5
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 132
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `17` | `17` | 41 | END | 41 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | Position_Unknown | `17` | `17` | 48 | START | 48 | 52 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `17` | `17` | 64 | START | 64 | 111 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `16` | `16` | 80 | START | 80 | 119 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `17` | `17` | 115 | START | 115 | 126 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `0` | `0` | 154 | START | 154 | 161 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–358 | 287 | 4 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–359 | 359 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–359 | 358 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–319 | 299 | 4 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–119 | 95 | 3 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–207 | 208 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–359 | 324 | 5 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–359 | 358 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–253 | 250 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–359 | 353 | 4 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–321 | 317 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–64 | 63 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–359 | 357 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–69 | 70 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–359 | 358 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–359 | 334 | 8 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–359 | 359 | 9 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–359 | 356 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–328 | 329 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–359 | 346 | 7 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–359 | 349 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 100–359 | 259 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 117–287 | 149 | 6 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 128–159 | 21 | 2 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 183–201 | 13 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 224–286 | 63 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 226–359 | 131 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 228–359 | 89 | 8 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 234–359 | 126 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 234–353 | 32 | 6 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 265–285 | 20 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 267–359 | 93 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 269–359 | 59 | 8 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 281–359 | 78 | 2 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 295–342 | 16 | 4 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 310–340 | 26 | 4 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 311–312 | 2 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 325–359 | 10 | 4 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 325–357 | 5 | 2 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 331–334 | 4 | 1 | Undefined position; Undefined team |
| `45` | `76` | Position_Unknown | Team_Unknown | 352–356 | 5 | 1 | Undefined position; Undefined team |
| `46` | `78` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |
| `47` | `79` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 35 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 114 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [162-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-358] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-203] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-333] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-301] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-92] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-119] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-266] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-314] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-245] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-336] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-181] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-321] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-359] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-355] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-328] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [48-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [64-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-328] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-51] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-254] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-304] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-344] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-234] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-167] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-165] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-287] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-191] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-215] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-286] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-230] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-248] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-257] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-265] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-359] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-239] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-305] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-353] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-272] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-285] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-287] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-312] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-315] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-335] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-340] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-345] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-359] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-309] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-322] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-313] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-322] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-340] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-312] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-327] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-339] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-353] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-359] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-327] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-357] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-334] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-356] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-358] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.

</details>