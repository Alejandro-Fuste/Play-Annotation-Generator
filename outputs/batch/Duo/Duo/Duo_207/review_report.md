# Play-Annotation-Generator Annotation Review — Duo_207

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_207`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `16` | `15` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_ComboBlock` | QB | offense | `4` | `4` |
| ✅ EXACT | `Action_ComboBlock` | TE1 | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 24 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 24 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 24 | START | 6 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 24 | START | 25 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 24 | START | 25 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `23` | `Group` | 24 | START | 25 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 24 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 24 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 24 | START | 0 | 46 |
| ✅ EXACT | `Action_ComboBlock` | RG | `16` | `15` | 47 | START | 47 | 58 |
| ✅ EXACT | `Action_ComboBlock` | RT | `21` | `20` | 47 | START | 47 | 93 |
| ✅ EXACT | `Action_ComboBlock` | QB | `4` | `4` | 47 | START | 47 | 93 |
| ✅ EXACT | `Action_ComboBlock` | TE1 | `7` | `7` | 47 | START | 47 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `16` | `15` | 59 | START | 59 | 65 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 93 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 46 | 23 | inferred_complete_timeline |
| `Action_ComboBlock` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 94 | 150 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 69 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 121 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 135 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 142 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 94 | 134 | 41 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 25–150
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 78 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 150 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 25–96
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 80 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 96 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 150 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 72 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 130 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–150
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 46 | 41 | inferred_complete_timeline |
| `Action_ComboBlock` | 47 | 58 | 12 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 150 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 25–116
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 46 | 22 | inferred_complete_timeline |
| `Action_ComboBlock` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 94 | 105 | 12 | inferred_complete_timeline |
| `Action_None` | 107 | 116 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 25–75
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 75 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 25–123
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 123 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 107 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 126 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 58 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 142 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 150 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 25–150
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 65 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 91 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 124 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 150 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 25–150
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 46 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 150 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 25–147
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 147 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 25–150
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 108 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 150 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–148 | 87 | 4 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–24 | 25 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–24 | 25 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–24 | 25 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–150 | 76 | 3 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–24 | 25 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–150 | 81 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 48–150 | 97 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 62–130 | 52 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 72–79 | 8 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 96–144 | 44 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 101–121 | 17 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 123–150 | 28 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 140–150 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `24` (actor_track_id `25`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 77 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-63] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-69] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-135] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-134] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-14] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-107] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-126] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-130] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-58] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-142] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-18] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [59-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-75] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-124] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-150] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-46] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-41] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-108] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-83] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-88] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-130] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-79] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-110] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-121] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-150] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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