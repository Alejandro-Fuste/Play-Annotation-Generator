# Play-Annotation-Generator Annotation Review — CrackToss_55

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_55`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 86
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE1 | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE2 | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | C | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `14` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `7` | `Group` | 0 | START | 0 | 13 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `19` | 104 | START | 119 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE1 | `11` | `10` | 107 | START | 107 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE2 | `10` | `9` | 107 | START | 107 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `2` | `1` | 107 | START | 107 | 115 |
| ✅ EXACT | `Action_SnapReceive` | C | `16` | `15` | 109 | END | 104 | 109 |
| ✅ EXACT | `Action_Toss` | C | `16` | `15` | 128 | START | 128 | 143 |
| ✅ EXACT | `Action_BallCarry` | RB | `14` | `13` | 144 | START | 144 | 194 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 143 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 194 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–13
- **Visible Samples:** 14

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_CrackBlock` | 107 | 128 | 22 | inferred_complete_timeline |
| `Action_CrackBlock` | 134 | 203 | 70 | inferred_complete_timeline |
| `Action_CrackBlock` | 209 | 225 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 110 | 190 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 120 | 17 | inferred_complete_timeline |
| `Action_None` | 130 | 195 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 104 | 109 | 6 | inferred_complete_timeline |
| `Action_None` | 110 | 127 | 18 | inferred_complete_timeline |
| `Action_Toss` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 144 | 164 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 123 | 20 | inferred_complete_timeline |
| `Action_None` | 128 | 202 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 225 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 119 | 16 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_None` | 132 | 139 | 8 | inferred_complete_timeline |
| `Action_None` | 143 | 166 | 24 | inferred_complete_timeline |
| `Action_None` | 171 | 225 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 225 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 115 | 12 | inferred_complete_timeline |
| `Action_None` | 120 | 202 | 83 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 225 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 169 | 66 | inferred_complete_timeline |
| `Action_None` | 175 | 207 | 33 | inferred_complete_timeline |
| `Action_None` | 212 | 225 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 141 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 120 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 205 | 102 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_None` | 215 | 222 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 103 | 104 | inferred_complete_timeline |
| `Action_None` | 104 | 165 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–170 | 170 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 44–148 | 105 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 119–144 | 26 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 137–140 | 4 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 139–209 | 71 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 152–225 | 71 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 168–225 | 58 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 174–225 | 47 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 180–225 | 46 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 197–225 | 29 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 201–225 | 25 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 212–225 | 14 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 219–225 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 104 != Inferred start 119
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 148 targets track ID '187', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 111: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=119, end=109. Clamping end to start.
- ⚠️ Action 'Action_None' range [104-225] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-115] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [117-170] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-202] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-205] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-225] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [110-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [107-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [134-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [209-225] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-202] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-127] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-148] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-144] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-176] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-225] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-196] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-225] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-225] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>