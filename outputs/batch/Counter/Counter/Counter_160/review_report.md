# Play-Annotation-Generator Annotation Review — Counter_160

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_160`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | TE | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF1 | defense | `5` | `4` |
| ✅ EXACT | `Action_DownBlock` | CB2 | defense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | WR2 | offense | `1` | `0` |
| ✅ EXACT | `Action_PullLeadBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | WR3 | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 17 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 46 |
| ✅ EXACT | `Action_BallSnap` | TE | `11` | `10` | 47 | START | 47 | 54 |
| ✅ EXACT | `Action_DownBlock` | TE | `11` | `10` | 55 | START | 55 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | SAF1 | `5` | `4` | 55 | START | 55 | 151 |
| ✅ EXACT | `Action_DownBlock` | CB2 | `6` | `5` | 55 | START | 55 | 151 |
| ✅ EXACT | `Action_PullBlock` | WR2 | `1` | `0` | 55 | START | 55 | 140 |
| ✅ EXACT | `Action_PullLeadBlock` | LG | `14` | `13` | 55 | START | 55 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | WR3 | `2` | `1` | 58 | START | 58 | 96 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 67 | END | 47 | 67 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 78 | START | 78 | 99 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `2` | `1` | 100 | START | 100 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 151 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 67 | 21 | inferred_complete_timeline |
| `Action_None` | 68 | 77 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 78 | 99 | 22 | inferred_complete_timeline |
| `Action_None` | 100 | 190 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 93 | 47 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PullBlock` | 55 | 140 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 58 | 96 | 39 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 210 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 151 | 97 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 46 | 22 | inferred_complete_timeline |
| `Action_None` | 47 | 49 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 17–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 54 | 38 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 55 | 151 | 97 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 110–210
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 110 | 160 | 51 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 102–210
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 102 | 210 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 32–210
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 32 | 46 | 15 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 105–109
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 105 | 109 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 132 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 172 | 126 | inferred_complete_timeline |
| `Action_None` | 176 | 203 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 94 | 48 | inferred_complete_timeline |
| `Action_None` | 99 | 210 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 151 | 97 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 55 | 151 | 97 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_None` | 47 | 210 | 164 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `24` | Position_Unknown | Team_Unknown | 122–194 | 70 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 138–210 | 73 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 146–210 | 64 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 154–210 | 57 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 181–192 | 5 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 191–201 | 4 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 202–207 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (SAF1) duration 97 frames exceeds threshold 90 frames [start=55, end=151].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (CB2) duration 97 frames exceeds threshold 90 frames [start=55, end=151].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (TE) duration 97 frames exceeds threshold 90 frames [start=55, end=151].
- ⚠️ Action 'Action_PullBlock' range [55-140] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [58-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [55-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-93] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-190] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-46] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [55-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-160] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-194] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '25' has 1 frames without a visible bounding box.
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