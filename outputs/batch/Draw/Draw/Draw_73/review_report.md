# Play-Annotation-Generator Annotation Review — Draw_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_73`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 47 | START | 47 | 61 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `13` | `12` | 50 | START | 62 | 148 |
| ✅ EXACT | `Action_PassBlock` | RT | `15` | `14` | 50 | START | 50 | 148 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `17` | 50 | START | 50 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `20` | 50 | START | 50 | 148 |
| ✅ EXACT | `Action_PassBlock` | LT | `22` | `21` | 50 | START | 50 | 148 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 61 | END | 47 | 61 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `20` | `19` | 73 | START | 73 | 100 |
| ✅ EXACT | `Action_BallCarry` | QB | `20` | `19` | 101 | START | 101 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 148 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_None` | 62 | 72 | 11 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 73 | 100 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 269 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 167 | 121 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 226 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 128 | 82 | inferred_complete_timeline |
| `Action_None` | 130 | 131 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 162 | 30 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 178 | 132 | inferred_complete_timeline |
| `Action_None` | 180 | 204 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 148 | 99 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 148 | 99 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 61 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 148 | 87 | inferred_complete_timeline |
| `Action_None` | 149 | 169 | 21 | inferred_complete_timeline |
| `Action_None` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 148 | 99 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 148 | 99 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 121 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 249 | 203 | inferred_complete_timeline |
| `Action_None` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 156 | 110 | inferred_complete_timeline |
| `Action_None` | 158 | 175 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 269 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 115 | 69 | inferred_complete_timeline |
| `Action_None` | 117 | 159 | 43 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_None` | 177 | 206 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 269 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 269 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 233 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 133 | 87 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 269 | 223 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 116–178 | 31 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 139–269 | 131 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 142–154 | 10 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 153–157 | 4 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 153–174 | 5 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 173–178 | 6 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 188–269 | 82 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 197–269 | 69 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 232–269 | 38 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 246–248 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `13` (C): Annotated start 50 != Inferred start 62
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 146: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 146: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [47–61], lower_priority='Action_PassBlock' annotated_start=50, effective_Action_PassBlock_start=62.
- ⚠️ Action 'Action_None' range [47-178] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-226] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-121] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-162] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-167] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-159] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-248] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>