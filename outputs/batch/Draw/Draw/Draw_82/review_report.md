# Play-Annotation-Generator Annotation Review — Draw_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_82`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 41 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 39 | START | 39 | 55 |
| ✅ EXACT | `Action_PassBlock` | RG | `14` | `13` | 42 | START | 42 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 42 | START | 56 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `22` | `21` | 42 | START | 42 | 65 |
| ✅ EXACT | `Action_PassBlock` | RT | `6` | `5` | 42 | START | 42 | 119 |
| ✅ EXACT | `Action_PassBlock` | LT | `8` | `7` | 42 | START | 42 | 119 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 55 | END | 39 | 55 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `19` | `18` | 59 | START | 59 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `19` | `18` | 91 | START | 91 | 113 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 119 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 55 | 17 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 59 | 90 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 113 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 140 | 102 | inferred_complete_timeline |
| `Action_None` | 147 | 239 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 162 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 206 | 168 | inferred_complete_timeline |
| `Action_None` | 209 | 215 | 7 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 119 | 78 | inferred_complete_timeline |
| `Action_None` | 120 | 137 | 18 | inferred_complete_timeline |
| `Action_None` | 139 | 239 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 65 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 68 | 81 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 83 | 119 | 37 | inferred_complete_timeline |
| `Action_None` | 120 | 150 | 31 | inferred_complete_timeline |
| `Action_None` | 152 | 239 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 39 | 55 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 85 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 119 | 78 | inferred_complete_timeline |
| `Action_None` | 120 | 239 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 119 | 78 | inferred_complete_timeline |
| `Action_None` | 120 | 130 | 11 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 149 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 77 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 103 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 87 | 49 | inferred_complete_timeline |
| `Action_None` | 89 | 239 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 156 | 118 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 228 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 239 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 51–68 | 10 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 59–239 | 121 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 95–239 | 135 | 3 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 109–124 | 8 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 126–239 | 114 | 1 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 156–164 | 9 | 1 | Undefined position; Undefined team |
| `28` | `46` | Position_Unknown | Team_Unknown | 169–239 | 69 | 2 | Undefined position; Undefined team |
| `29` | `47` | Position_Unknown | Team_Unknown | 174–239 | 65 | 2 | Undefined position; Undefined team |
| `30` | `49` | Position_Unknown | Team_Unknown | 175–233 | 34 | 6 | Undefined position; Undefined team |
| `31` | `51` | Position_Unknown | Team_Unknown | 185–187 | 3 | 1 | Undefined position; Undefined team |
| `32` | `54` | Position_Unknown | Team_Unknown | 204–205 | 2 | 1 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `34` | `58` | Position_Unknown | Team_Unknown | 228–230 | 3 | 1 | Undefined position; Undefined team |
| `35` | `59` | Position_Unknown | Team_Unknown | 229–230 | 2 | 1 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [39–55], lower_priority='Action_PassBlock' annotated_start=42, effective_Action_PassBlock_start=56.
- ⚠️ Action 'Action_None' range [39-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-149] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-206] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-87] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-103] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-65] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [68-81] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-239] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-197] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-198] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-233] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '36' has 1 frames without a visible bounding box.
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

</details>