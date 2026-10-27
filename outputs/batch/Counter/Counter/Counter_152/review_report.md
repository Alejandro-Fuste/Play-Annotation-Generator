# Play-Annotation-Generator Annotation Review — Counter_152

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_152`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 157
- **Validation Warnings:** 206
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 127
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | OLB | defense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | OLB | defense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | OLB | defense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_Handoff` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 11 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 13 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 166 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `6` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_BallSnap` | OLB | `2` | `1` | 123 | START | 123 | 125 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | OLB | `2` | `1` | 126 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_PullBlock` | Position_Unknown | `7` | `6` | 126 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | OLB | `2` | `1` | 126 | START | 126 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 127 | END | 123 | 127 |
| ⚠️ START CHANGED | `Action_Handoff` | QB | `10` | `9` | 156 | START | 168 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `4` | 172 | START | 172 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 228 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 11–332
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 20 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 34 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 63 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 122 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 123 | 127 | 5 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 200 | 10 | inferred_complete_timeline |
| `Action_None` | 204 | 213 | 10 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 312 | 79 | inferred_complete_timeline |
| `Action_None` | 317 | 332 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 179 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 205 | 210 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 213 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 276 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 122 | 54 | inferred_complete_timeline |
| `Action_None` | 123 | 135 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–261
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 55 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 64 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 122 | 28 | inferred_complete_timeline |
| `Action_None` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 221 | 17 | inferred_complete_timeline |
| `Action_None` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 236 | 243 | 8 | inferred_complete_timeline |
| `Action_None` | 245 | 249 | 5 | inferred_complete_timeline |
| `Action_None` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 165 | 43 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_BallSnap` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 126 | 169 | 44 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 228 | 228 | 1 | inferred_complete_timeline |
| `Action_None` | 229 | 231 | 3 | inferred_complete_timeline |
| `Action_None` | 244 | 292 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 225 | 103 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 260 | 276 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_None` | 123 | 213 | 91 | inferred_complete_timeline |
| `Action_None` | 215 | 220 | 6 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 227 | 233 | 7 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 249 | 10 | inferred_complete_timeline |
| `Action_None` | 252 | 261 | 10 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–114 | 41 | 5 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 2–283 | 123 | 11 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 10–13 | 4 | 1 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 18–36 | 12 | 3 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 50–169 | 103 | 7 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 90–91 | 2 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 107–150 | 26 | 6 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 146–280 | 90 | 4 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 162–294 | 87 | 8 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 165–292 | 128 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 169–266 | 98 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 173–359 | 186 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 186–298 | 93 | 6 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 201–307 | 87 | 4 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 203–224 | 12 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 204–260 | 56 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 204–223 | 20 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 205–213 | 8 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 205–304 | 68 | 7 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 216–359 | 143 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 231–232 | 2 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 234–249 | 15 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 237–271 | 17 | 4 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 244–246 | 3 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 261–288 | 21 | 2 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 263–284 | 22 | 1 | Undefined position; Undefined team |
| `34` | `51` | Position_Unknown | Team_Unknown | 265–278 | 13 | 2 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 277–359 | 82 | 2 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 348–352 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `2` (OLB)
- ❌ Missing segment for action `Action_PullBlock` on target `7` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (4 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `10` (QB): Annotated start 156 != Inferred start 168
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 145 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Overlapping action conflict at frame 126 for track '1': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Segment 'Action_PullBlock' for track '6' has invalid range: start=126, end=114. Clamping end to start.
- ⚠️ Action 'Action_None' range [123-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [126-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [172-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [189-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-292] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-165] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-276] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-276] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-30] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-114] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-25] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-246] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-257] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-13] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-20] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-91] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [123-127] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [168-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-200] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-312] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-332] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-243] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-26] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-36] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-137] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-128] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-233] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-274] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-294] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-292] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-266] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-286] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-222] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-274] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-298] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-223] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-307] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-260] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-207] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-247] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-273] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-304] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-354] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-271] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-276] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-284] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>