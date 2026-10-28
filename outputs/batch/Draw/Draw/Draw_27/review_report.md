# Play-Annotation-Generator Annotation Review — Draw_27

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_27`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 89
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
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 11 | START | 11 | 25 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `15` | 14 | START | 14 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `17` | 14 | START | 26 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `18` | 14 | START | 14 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `19` | 14 | START | 14 | 40 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `4` | 14 | START | 14 | 86 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 25 | END | 11 | 25 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `8` | `7` | 30 | START | 30 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `7` | 56 | START | 56 | 80 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 30 | 55 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 80 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 134 | 124 | inferred_complete_timeline |
| `Action_None` | 141 | 166 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 161 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 200 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 86 | 73 | inferred_complete_timeline |
| `Action_None` | 87 | 149 | 63 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 166 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 40 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 86 | 31 | inferred_complete_timeline |
| `Action_None` | 87 | 223 | 137 | inferred_complete_timeline |
| `Action_None` | 229 | 239 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 71 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 86 | 14 | inferred_complete_timeline |
| `Action_None` | 87 | 162 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 86 | 73 | inferred_complete_timeline |
| `Action_None` | 87 | 158 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 86 | 73 | inferred_complete_timeline |
| `Action_None` | 87 | 150 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 208 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 41 | 31 | inferred_complete_timeline |
| `Action_None` | 46 | 82 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 107 | 97 | inferred_complete_timeline |
| `Action_None` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 52 | 42 | inferred_complete_timeline |
| `Action_None` | 58 | 61 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 239 | 229 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 27 | 17 | inferred_complete_timeline |
| `Action_None` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_None` | 32 | 163 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 146 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 59 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 219 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 136 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 210 | 200 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 47–55 | 9 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 70–190 | 109 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 71–228 | 108 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 92–217 | 103 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 111–149 | 12 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 131–132 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 156–239 | 83 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 173–200 | 24 | 5 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 188–239 | 52 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 194–239 | 46 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [11–25], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=26.
- ⚠️ Action 'Action_None' range [11-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-107] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-208] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-52] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-219] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [11-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-223] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-228] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '34' has 1 frames without a visible bounding box.
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