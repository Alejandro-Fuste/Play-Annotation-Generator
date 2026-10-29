# Play-Annotation-Generator Annotation Review — Duo_180

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_180`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 67
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `24` | `24` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 4 | START | 4 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 4 | START | 4 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 4 | START | 4 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 4 | START | 4 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 4 | START | 4 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 4 | START | 4 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `22` | `Group` | 4 | START | 4 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `24` | `Group` | 4 | START | 4 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 4 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 4 | START | 4 | 100 |
| ✅ EXACT | `Action_ComboBlock` | LT | `16` | `16` | 51 | START | 51 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `19` | `19` | 51 | START | 51 | 56 |
| ✅ EXACT | `Action_ComboBlock` | C | `24` | `24` | 51 | START | 51 | 81 |
| ✅ EXACT | `Action_ComboBlock` | RG | `4` | `4` | 51 | START | 51 | 81 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 81 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 4–86
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 86 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–100
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 58 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 100 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–100
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 100 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 4–85
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 85 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 4–100
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 100 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 4–100
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 50 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 92 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 4–100
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 50 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 51 | 56 | 6 | inferred_complete_timeline |
| `Action_ComboBlock` | 58 | 68 | 11 | inferred_complete_timeline |
| `Action_ComboBlock` | 73 | 81 | 9 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `24`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 4–100
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 50 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 100 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_ComboBlock` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 100 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 4–100
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 100 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 4–100
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 51 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 100 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–100
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 100 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `23`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 4–85
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 40 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 65 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 80 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 85 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 100 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 4–100
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 100 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 4–83
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 61 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 83 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–87
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 69 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 79 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 87 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 4–100
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 53 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 61 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 73 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 100 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–82 | 7 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–98 | 97 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–3 | 4 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 2–3 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 50–100 | 51 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 52–94 | 39 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 62–85 | 24 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 84–100 | 14 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 92–99 | 6 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 94–100 | 7 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 97–100 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 59 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-100] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-66] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-58] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-53] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-73] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-100] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [51-56] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [58-68] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-86] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-61] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-83] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-40] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-65] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-80] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-59] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-75] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-94] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-85] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-87] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-90] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-100] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-95] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-100] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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