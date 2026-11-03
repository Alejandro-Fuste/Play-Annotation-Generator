# Play-Annotation-Generator Annotation Review — OutAndUp_20

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_20`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Rec`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_SellOut` | TE2 | offense | `4` | `4` |
| ✅ EXACT | `Action_RunGoRoute` | TE2 | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `8` | `Group` | 0 | START | 0 | 12 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `17` | `17` | 22 | START | 34 | 39 |
| ✅ EXACT | `Action_PassBlock` | LG | `12` | `12` | 25 | START | 25 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 25 | START | 93 | 95 |
| ✅ EXACT | `Action_PassBlock` | LT | `2` | `2` | 25 | START | 25 | 112 |
| ✅ EXACT | `Action_PassBlock` | RT | `6` | `6` | 25 | START | 25 | 248 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 39 | END | 22 | 39 |
| ✅ EXACT | `Action_SellOut` | TE2 | `4` | `4` | 55 | START | 55 | 84 |
| ✅ EXACT | `Action_RunGoRoute` | TE2 | `4` | `4` | 85 | START | 85 | 125 |
| ✅ EXACT | `Action_ThrowPass` | QB | `1` | `1` | 98 | START | 98 | 109 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 39 | 18 | inferred_complete_timeline |
| `Action_None` | 40 | 97 | 58 | inferred_complete_timeline |
| `Action_ThrowPass` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 174 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 127 | 106 | inferred_complete_timeline |
| `Action_None` | 133 | 221 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–12
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_SellOut` | 55 | 84 | 30 | inferred_complete_timeline |
| `Action_RunGoRoute` | 85 | 125 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 112 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 150 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 102 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 248 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 80 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 75 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 34 | 13 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_None` | 61 | 87 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 84 | 63 | inferred_complete_timeline |
| `Action_None` | 103 | 144 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 62 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 167 | 146 | inferred_complete_timeline |
| `Action_None` | 169 | 211 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 264 | 243 | inferred_complete_timeline |
| `Action_None` | 267 | 299 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 178 | 157 | inferred_complete_timeline |
| `Action_None` | 181 | 200 | 20 | inferred_complete_timeline |
| `Action_None` | 207 | 299 | 93 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 19–26 | 6 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 34–152 | 110 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 49–118 | 70 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 87–253 | 148 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 94–222 | 123 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 101–112 | 12 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 118–258 | 119 | 11 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 121–233 | 111 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 128–299 | 172 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 137–140 | 4 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 148–204 | 57 | 1 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 150–299 | 147 | 3 | Undefined position; Undefined team |
| `28` | `28` | Position_Unknown | Team_Unknown | 159–299 | 141 | 1 | Undefined position; Undefined team |
| `29` | `29` | Position_Unknown | Team_Unknown | 168–214 | 47 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 274–288 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `17` (Position_Unknown): Annotated start 22 != Inferred start 34
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 63 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [22-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-211] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-264] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellOut' range [55-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [85-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-127] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-200] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-144] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 22, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [22-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-118] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-97] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-157] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-253] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-167] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-112] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-216] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-204] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-288] for track '31' has 1 frames without a visible bounding box.
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