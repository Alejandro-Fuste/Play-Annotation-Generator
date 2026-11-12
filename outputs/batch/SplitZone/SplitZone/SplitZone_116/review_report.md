# Play-Annotation-Generator Annotation Review — SplitZone_116

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_116`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 2 | START | 3 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 2 | START | 3 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 2 | START | 3 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 2 | START | 3 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 2 | START | 3 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 2 | START | 3 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 2 | START | 3 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 2 | START | 3 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `4` | 28 | START | 28 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 31 | START | 31 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 31 | START | 31 | 46 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `3` | `3` | 31 | START | 31 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `4` | `4` | 31 | START | 39 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `6` | 31 | START | 31 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `10` | `10` | 32 | START | 32 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | QB | `8` | `8` | 38 | END | 28 | 33 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 42 | START | 42 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `14` | 56 | START | 56 | 100 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 126 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 38 | 1 | inferred_complete_timeline |
| `Action_None` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 42 | 55 | 14 | inferred_complete_timeline |
| `Action_None` | 56 | 224 | 169 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 15 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 55 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 100 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 31 | 29 | inferred_complete_timeline |
| `Action_SplitBlock` | 32 | 56 | 25 | inferred_complete_timeline |
| `Action_SplitBlock` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_SplitBlock` | 75 | 126 | 52 | inferred_complete_timeline |
| `Action_None` | 127 | 212 | 86 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–239
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 9 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 30 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 48 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 115 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 239 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–59
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 30 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 59 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 38 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 88 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 126 | 37 | inferred_complete_timeline |
| `Action_None` | 127 | 239 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 3–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 30 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 59 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 98 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 107 | 126 | 20 | inferred_complete_timeline |
| `Action_None` | 127 | 208 | 82 | inferred_complete_timeline |
| `Action_None` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 3–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 30 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 31 | 126 | 96 | inferred_complete_timeline |
| `Action_None` | 127 | 239 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 3–184
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_None` | 28 | 184 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 3–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_None` | 28 | 239 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_None` | 28 | 166 | 139 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_None` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_None` | 36 | 85 | 50 | inferred_complete_timeline |
| `Action_None` | 88 | 103 | 16 | inferred_complete_timeline |
| `Action_None` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_None` | 28 | 196 | 169 | inferred_complete_timeline |
| `Action_None` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 27 | 25 | inferred_complete_timeline |
| `Action_None` | 28 | 168 | 141 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 3–29 | 27 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 72–239 | 167 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 82–239 | 156 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 86–239 | 151 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 89–94 | 6 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 94–197 | 104 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 100–239 | 137 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 116–117 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 130–162 | 24 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 136–239 | 104 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 146–239 | 94 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 153–232 | 75 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 159–239 | 80 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 168–239 | 72 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 176–208 | 33 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 190–193 | 4 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 225–239 | 10 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (C) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [28–38], lower_priority='Action_ZoneBlock' annotated_start=31, effective_Action_ZoneBlock_start=39.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 96 frames exceeds threshold 90 frames [start=31, end=126].
- ⚠️ Action 'Action_None' range [28-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-43] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-166] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-59] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [62-98] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-33] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [28-33] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-239] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [32-56] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [59-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-9] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-115] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [31-46] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-15] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-100] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-96] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-239] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-197] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-169] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-193] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-234] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>