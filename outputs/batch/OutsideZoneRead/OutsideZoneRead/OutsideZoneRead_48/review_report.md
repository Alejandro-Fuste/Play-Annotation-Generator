# Play-Annotation-Generator Annotation Review — OutsideZoneRead_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_48`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_PressEdge` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_ReadEdgeDefender` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | RG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 261 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 153 | START | 153 | 164 |
| ✅ EXACT | `Action_ZoneBlock` | C | `15` | `15` | 153 | START | 153 | 201 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | RT | `2` | `2` | 153 | START | 155 | 201 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `4` | `4` | 153 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `9` | 153 | START | 153 | 201 |
| ❌ MISSING SEGMENT | `Action_PressEdge` | Position_Unknown | `21` | `21` | 165 | START | N/A | N/A |
| ✅ EXACT | `Action_ReadEdgeDefender` | RG | `12` | `12` | 165 | START | 165 | 176 |
| ✅ EXACT | `Action_Handoff` | RG | `12` | `12` | 177 | START | 177 | 188 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 225 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 41 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 78 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 162 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 201 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 266 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 201 | 49 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 95 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 201 | 49 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 135 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 164 | 12 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 165 | 176 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 177 | 188 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 201 | 47 | inferred_complete_timeline |
| `Action_None` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 269 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 149 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 114 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 119–139 | 17 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 120–258 | 127 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 138–269 | 132 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 161–269 | 109 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 162–264 | 99 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 178–269 | 92 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 189–269 | 68 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 211–269 | 49 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 219–269 | 51 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 225–235 | 11 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 244–258 | 11 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 250–269 | 20 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `2` (RT): Annotated start 153 != Inferred start 155
- ❌ Missing segment for action `Action_ZoneBlock` on target `4` (LT)
- ❌ Missing segment for action `Action_PressEdge` on target `21` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '4' has invalid range: start=153, end=95. Clamping end to start.
- ⚠️ Segment 'Action_PressEdge' for track '21' has invalid range: start=165, end=160. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-191] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-114] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [177-188] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-225] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-41] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-162] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-201] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-266] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-127] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-158] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-258] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-261] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-216] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-228] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-235] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-258] for track '29' has 1 frames without a visible bounding box.
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

</details>