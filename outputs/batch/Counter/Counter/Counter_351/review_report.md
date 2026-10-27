# Play-Annotation-Generator Annotation Review — Counter_351

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_351`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `20` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 83 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 81 | START | 81 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 84 | START | 95 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `19` | `18` | 84 | START | 84 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `21` | `20` | 84 | START | 84 | 107 |
| ✅ EXACT | `Action_PullBlock` | LG | `22` | `21` | 84 | START | 84 | 158 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `8` | `7` | 84 | START | 84 | 158 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 94 | END | 81 | 94 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 106 | START | 106 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 125 | START | 125 | 143 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 158 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_SnapReceive` | 81 | 94 | 14 | inferred_complete_timeline |
| `Action_None` | 95 | 105 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 106 | 124 | 19 | inferred_complete_timeline |
| `Action_None` | 125 | 171 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 143 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 196 | 43 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 167 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 238 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 192 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 84 | 158 | 75 | inferred_complete_timeline |
| `Action_None` | 159 | 195 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 192 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PullBlock` | 84 | 158 | 75 | inferred_complete_timeline |
| `Action_None` | 159 | 179 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_BallSnap` | 81 | 94 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 95 | 122 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 142 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 158 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 184 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 103 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 114 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_DownBlock` | 84 | 107 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 158 | 49 | inferred_complete_timeline |
| `Action_None` | 159 | 211 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 203 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 124 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 189 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 184 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 159 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 239 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 191 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 196 | 116 | inferred_complete_timeline |
| `Action_None` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_None` | 81 | 205 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–179 | 173 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 37–70 | 34 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 121–153 | 33 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 137–140 | 4 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 157–198 | 42 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 165–176 | 12 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 174–176 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 176–195 | 18 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 177–181 | 5 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 704: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [81–94], lower_priority='Action_DownBlock' annotated_start=84, effective_Action_DownBlock_start=95.
- ⚠️ Action 'Action_None' range [81-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-124] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [154-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [106-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-195] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-191] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [95-122] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-184] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [84-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-70] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-153] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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