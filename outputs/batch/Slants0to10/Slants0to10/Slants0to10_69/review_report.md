# Play-Annotation-Generator Annotation Review — Slants0to10_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_69`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 109
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 1 | START | 1 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 4 | START | 4 | 82 |
| ✅ EXACT | `Action_PassBlock` | LG | `17` | `17` | 4 | START | 4 | 239 |
| ✅ EXACT | `Action_PassBlock` | RT | `19` | `19` | 4 | START | 4 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 4 | START | 4 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 4 | START | 18 | 70 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `1` | `1` | 17 | START | 17 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 17 | END | 1 | 17 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 66 | START | 66 | 73 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 104 | START | 104 | 116 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_None` | 18 | 65 | 48 | inferred_complete_timeline |
| `Action_ThrowPass` | 66 | 73 | 8 | inferred_complete_timeline |
| `Action_None` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_None` | 86 | 95 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 106 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 17 | 88 | 72 | inferred_complete_timeline |
| `Action_None` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 116 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 172 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 82 | 79 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 112 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 239 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 70 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 93 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 59 | 56 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 100 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 207 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 94 | 94 | inferred_complete_timeline |
| `Action_None` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_None` | 116 | 143 | 28 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |
| `Action_None` | 162 | 170 | 9 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 54 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 75 | 75 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 239 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 39 | 39 | inferred_complete_timeline |
| `Action_None` | 42 | 128 | 87 | inferred_complete_timeline |
| `Action_None` | 133 | 136 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 88 | 88 | inferred_complete_timeline |
| `Action_None` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 192 | 88 | inferred_complete_timeline |
| `Action_None` | 194 | 237 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 70 | 70 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_None` | 97 | 206 | 110 | inferred_complete_timeline |
| `Action_None` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 109 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 239 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 176 | 176 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 63 | 63 | inferred_complete_timeline |
| `Action_None` | 69 | 100 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 71–239 | 147 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–86 | 6 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 99–115 | 14 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 107–239 | 117 | 5 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 113–239 | 111 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 116–118 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 118–239 | 93 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 158–239 | 82 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 168–239 | 59 | 9 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 204–239 | 36 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 217–225 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [1–17], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=18.
- ⚠️ Action 'Action_None' range [1-88] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-192] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-237] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-94] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-111] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-143] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-54] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-172] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-75] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-128] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-239] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-52] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-176] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-82] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-95] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-70] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-207] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-59] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-75] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-120] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-115] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-151] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-140] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-237] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '34' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>