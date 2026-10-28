# Play-Annotation-Generator Annotation Review — Draw_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_53`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_PassBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `2` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `21` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 40 | START | 40 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `15` | 43 | START | 44 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `16` | 43 | START | 46 | 50 |
| ⚠️ START CHANGED | `Action_PassBlock` | LG | `19` | `18` | 43 | START | 46 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `18` | 43 | START | 46 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `19` | 43 | START | 43 | 53 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 56 | END | 40 | 56 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `7` | `6` | 60 | START | 60 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `6` | 85 | START | 85 | 96 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 106 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_None` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 60 | 84 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 192 | 78 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 111 | 72 | inferred_complete_timeline |
| `Action_None` | 113 | 118 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_None` | 64 | 154 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 169 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 83 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 107 | 170 | 64 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 49 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 55 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 53 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 89 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 133 | 19 | inferred_complete_timeline |
| `Action_None` | 138 | 147 | 10 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 83 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 85 | 106 | 22 | inferred_complete_timeline |
| `Action_None` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_None` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 181 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 55 | 16 | inferred_complete_timeline |
| `Action_None` | 58 | 75 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 42 | 103 | 62 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 161 | 171 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 44 | 168 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 147 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 156 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 133 | 94 | inferred_complete_timeline |
| `Action_None` | 136 | 210 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 131 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 96 | 57 | inferred_complete_timeline |
| `Action_None` | 106 | 190 | 85 | inferred_complete_timeline |
| `Action_None` | 192 | 199 | 8 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–119 | 116 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 2–210 | 190 | 8 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 67–188 | 89 | 5 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 68–174 | 90 | 6 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 81–85 | 5 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 118–147 | 23 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 123–210 | 88 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 138–210 | 73 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 146–159 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `19` (LG): Annotated start 43 != Inferred start 46
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [40–55], lower_priority='Action_PassBlock' annotated_start=43, effective_Action_PassBlock_start=56.
- ⚠️ Action 'Action_None' range [40-104] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-169] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-61] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [105-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-55] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-131] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '9' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-168] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-103] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-83] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [85-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-83] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-170] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [40-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-53] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-89] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [92-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-106] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-133] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-147] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-188] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-171] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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