# Play-Annotation-Generator Annotation Review — InsideZoneRead_375

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_375`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | LB1 | defense | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | LB1 | defense | `10` | `9` |
| ✅ EXACT | `Action_Keep` | LB1 | defense | `10` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 10 |
| ✅ EXACT | `Action_BallSnap` | RB | `11` | `10` | 11 | START | 11 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 14 | START | 14 | 27 |
| ✅ EXACT | `Action_SnapReceive` | LB1 | `10` | `9` | 25 | END | 11 | 25 |
| ✅ EXACT | `Action_ReadDefender` | LB1 | `10` | `9` | 29 | START | 29 | 34 |
| ✅ EXACT | `Action_Keep` | LB1 | `10` | `9` | 35 | START | 35 | 54 |
| ✅ EXACT | `Action_BlockSecondLevel` | RB | `11` | `10` | 36 | START | 36 | 56 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `10` | `9` | 55 | START | 55 | 68 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 76 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 52 | 42 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 161 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_BallSnap` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 35 | 10 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 36 | 56 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 143 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 84 | 74 | inferred_complete_timeline |
| `Action_None` | 86 | 180 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 14 | 27 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 35 | 7 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 130 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_SnapReceive` | 11 | 25 | 15 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 29 | 34 | 6 | inferred_complete_timeline |
| `Action_Keep` | 35 | 54 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 55 | 68 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 61 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 113 | 103 | inferred_complete_timeline |
| `Action_None` | 116 | 122 | 7 | inferred_complete_timeline |
| `Action_None` | 124 | 164 | 41 | inferred_complete_timeline |
| `Action_None` | 168 | 175 | 8 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 169 | 159 | inferred_complete_timeline |
| `Action_None` | 173 | 177 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 180 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_None` | 11 | 161 | 151 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 14–34 | 19 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 27–38 | 10 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 30–33 | 4 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 30–34 | 5 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 30–33 | 4 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 33–51 | 19 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 60–180 | 55 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 64–77 | 14 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 99–180 | 82 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 101–180 | 80 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 106–180 | 72 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 116–144 | 19 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 117–164 | 45 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 117–166 | 39 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 149–155 | 7 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 152–180 | 29 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 165–169 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 57 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [11-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-143] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [36-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-52] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-161] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [14-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-34] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-33] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-33] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-153] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_375'; source metadata written as null.

</details>