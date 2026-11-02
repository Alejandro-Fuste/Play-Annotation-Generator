# Play-Annotation-Generator Annotation Review — JetSweep_197

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_197`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 124
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `4` | `3` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Toss` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `4` | `3` | 61 | START | 61 | 127 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 105 | START | 105 | 116 |
| ✅ EXACT | `Action_LeadBlock` | TE | `10` | `9` | 106 | START | 106 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `17` | 106 | START | 106 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `20` | `19` | 106 | START | 106 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 106 | START | 106 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 106 | START | 117 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 116 | END | 105 | 116 |
| ✅ EXACT | `Action_Toss` | QB | `2` | `1` | 121 | START | 121 | 127 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `4` | `3` | 128 | START | 128 | 354 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 151 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_SnapReceive` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_Toss` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_None` | 128 | 359 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 148 | 44 | inferred_complete_timeline |
| `Action_None` | 151 | 359 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–281
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 281 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_JetMotion` | 61 | 127 | 67 | inferred_complete_timeline |
| `Action_BallCarry` | 128 | 354 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_LeadBlock` | 106 | 151 | 46 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 359 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 136 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 105 | 116 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 151 | 29 | inferred_complete_timeline |
| `Action_None` | 152 | 359 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 112 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 129 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 151 | 18 | inferred_complete_timeline |
| `Action_None` | 152 | 194 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 151 | 46 | inferred_complete_timeline |
| `Action_None` | 152 | 165 | 14 | inferred_complete_timeline |
| `Action_None` | 169 | 359 | 191 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–355
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 163 | 59 | inferred_complete_timeline |
| `Action_None` | 165 | 355 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 279 | 175 | inferred_complete_timeline |
| `Action_None` | 281 | 358 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 207 | 103 | inferred_complete_timeline |
| `Action_None` | 212 | 306 | 95 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 318 | 7 | inferred_complete_timeline |
| `Action_None` | 320 | 324 | 5 | inferred_complete_timeline |
| `Action_None` | 327 | 359 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 315 | 211 | inferred_complete_timeline |
| `Action_None` | 318 | 359 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 198 | 94 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 359 | 255 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–132 | 133 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 68–71 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 150–359 | 202 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 152–164 | 12 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 170–181 | 8 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 173–358 | 147 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 210–359 | 142 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 247–252 | 6 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 266–359 | 81 | 6 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 268–359 | 58 | 9 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 270–359 | 90 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 276–359 | 81 | 2 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 283–359 | 76 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 298–355 | 32 | 8 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 323–341 | 9 | 3 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 349–354 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 396: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [105–116], lower_priority='Action_ZoneBlock' annotated_start=106, effective_Action_ZoneBlock_start=117.
- ⚠️ Action 'Action_None' range [105-281] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-359] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [128-354] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-207] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-306] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-318] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-315] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-359] for track '6' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-279] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-358] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-163] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-198] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-136] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-359] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-165] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-112] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-194] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-359] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-353] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-208] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-249] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-358] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-252] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-283] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-302] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-333] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-354] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-283] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-305] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-332] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-352] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-323] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-359] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-354] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-334] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-345] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-330] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>