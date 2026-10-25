# Play-Annotation-Generator Annotation Review — BootPass_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 63
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `1` | `1` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `26` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 47 | START | 47 | 62 |
| ✅ EXACT | `Action_RunBlock` | LG | `1` | `1` | 53 | START | 53 | 161 |
| ✅ EXACT | `Action_RunBlock` | RT | `10` | `10` | 53 | START | 53 | 162 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `12` | `12` | 53 | START | 63 | 164 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `4` | `4` | 53 | START | 53 | 66 |
| ✅ EXACT | `Action_RunBlock` | LT | `5` | `5` | 53 | START | 53 | 130 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 62 | END | 47 | 62 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `6` | `6` | 65 | START | 65 | 83 |
| ✅ EXACT | `Action_BootAway` | QB | `6` | `6` | 84 | START | 84 | 109 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 143 | START | 143 | 152 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `26` | `22` | 184 | START | 184 | 210 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 62 | 16 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 65 | 83 | 19 | inferred_complete_timeline |
| `Action_BootAway` | 84 | 109 | 26 | inferred_complete_timeline |
| `Action_None` | 110 | 142 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_None` | 153 | 166 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 160 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 155 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 130 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 161 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 62 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 63 | 164 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 66 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 70 | 160 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 162 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 102 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 87 | 41 | inferred_complete_timeline |
| `Action_None` | 97 | 162 | 66 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 105 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 46 | 34 | inferred_complete_timeline |
| `Action_None` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_None` | 60 | 109 | 50 | inferred_complete_timeline |
| `Action_None` | 112 | 156 | 45 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 159 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 116 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 76 | 30 | inferred_complete_timeline |
| `Action_None` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_None` | 86 | 88 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 67–210 | 144 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 82–168 | 87 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 133–153 | 21 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 157–167 | 11 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 162–210 | 49 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 163–210 | 48 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 165–210 | 46 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 179–197 | 13 | 4 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 183–185 | 3 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 77 | 79 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `12` (C): Annotated start 53 != Inferred start 63
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [47–62], lower_priority='Action_RunBlock' annotated_start=53, effective_Action_RunBlock_start=63.
- ⚠️ Action 'Action_None' range [47-116] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-66] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [70-160] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-102] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [63-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-162] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-168] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-153] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [184-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-197] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>