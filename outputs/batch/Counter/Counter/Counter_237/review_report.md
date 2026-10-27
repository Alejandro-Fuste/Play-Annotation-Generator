# Play-Annotation-Generator Annotation Review — Counter_237

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_237`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 58
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 86 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 87 | START | 87 | 106 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 89 | START | 89 | 169 |
| ✅ EXACT | `Action_DownBlock` | LG | `17` | `16` | 89 | START | 89 | 102 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `19` | `18` | 89 | START | 107 | 169 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `20` | 89 | START | 89 | 169 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `18` | `17` | 89 | START | 89 | 169 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 106 | END | 87 | 106 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 115 | START | 115 | 128 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `22` | `21` | 129 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 169 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 87 | 106 | 20 | inferred_complete_timeline |
| `Action_None` | 107 | 114 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 115 | 128 | 14 | inferred_complete_timeline |
| `Action_None` | 129 | 269 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 266 | 180 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 266 | 97 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 102 | 14 | inferred_complete_timeline |
| `Action_None` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 87 | 106 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 169 | 63 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PullBlock` | 89 | 169 | 81 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 171 | 85 | inferred_complete_timeline |
| `Action_None` | 183 | 184 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 159 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 153 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 159 | 73 | inferred_complete_timeline |
| `Action_None` | 165 | 179 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 155 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 185 | 99 | inferred_complete_timeline |
| `Action_None` | 190 | 269 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 247 | 161 | inferred_complete_timeline |
| `Action_None` | 249 | 254 | 6 | inferred_complete_timeline |
| `Action_None` | 256 | 266 | 11 | inferred_complete_timeline |
| `Action_None` | 269 | 269 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 155 | 69 | inferred_complete_timeline |
| `Action_None` | 158 | 269 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 251 | 165 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 215 | 129 | inferred_complete_timeline |
| `Action_None` | 218 | 269 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 123–246 | 116 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 124–269 | 128 | 5 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 169–269 | 101 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 176–269 | 94 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 195–269 | 66 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 218–235 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `19` (C): Annotated start 89 != Inferred start 107
- ❌ Missing segment for action `Action_BallCarry` on target `22` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [87–106], lower_priority='Action_DownBlock' annotated_start=89, effective_Action_DownBlock_start=107.
- ⚠️ Segment 'Action_BallCarry' for track '21' has invalid range: start=129, end=117. Clamping end to start.
- ⚠️ Action 'Action_None' range [87-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-251] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-266] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-269] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-247] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-266] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-159] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [89-169] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-238] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-185] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '29' has 1 frames without a visible bounding box.
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

</details>