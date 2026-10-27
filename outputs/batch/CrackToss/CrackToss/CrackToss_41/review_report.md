# Play-Annotation-Generator Annotation Review — CrackToss_41

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `CrackToss_41`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 88
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | SAF | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE2 | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `11` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 68 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 69 | START | 69 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | SAF | `5` | `4` | 72 | START | 72 | 186 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | TE2 | `3` | `2` | 72 | START | 72 | 185 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `6` | `5` | 72 | START | 72 | 198 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 77 | END | 69 | 77 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 78 | START | 78 | 87 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `11` | `10` | 88 | START | 88 | 185 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_SnapReceive` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_Toss` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 88 | 200 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 145 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 185 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 200 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PullBlock` | 72 | 185 | 114 | inferred_complete_timeline |
| `Action_PullBlock` | 187 | 200 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 68 | 50 | inferred_complete_timeline |
| `Action_None` | 69 | 195 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 68 | 50 | inferred_complete_timeline |
| `Action_None` | 69 | 104 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_BallSnap` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_None` | 78 | 119 | 42 | inferred_complete_timeline |
| `Action_None` | 121 | 200 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 200 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 161 | 93 | inferred_complete_timeline |
| `Action_None` | 163 | 183 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 17 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 68 | 50 | inferred_complete_timeline |
| `Action_None` | 69 | 200 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 165 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 185 | 117 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 100 | 32 | inferred_complete_timeline |
| `Action_None` | 104 | 200 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 163 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 142 | 74 | inferred_complete_timeline |
| `Action_None` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 176 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 95 | 27 | inferred_complete_timeline |
| `Action_None` | 97 | 121 | 25 | inferred_complete_timeline |
| `Action_None` | 166 | 199 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 200 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 164 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_None` | 69 | 200 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_CrackBlock` | 72 | 186 | 115 | inferred_complete_timeline |
| `Action_CrackBlock` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–198 | 199 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 93–194 | 80 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 100–129 | 9 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 102–196 | 91 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 160–178 | 7 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 170–200 | 26 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 173–174 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 174–188 | 5 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 195–200 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_None' at frame 126 targets track ID '160', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 84: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (TE2) duration 129 frames exceeds threshold 90 frames [start=72, end=200].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (Unknown) duration 127 frames exceeds threshold 90 frames [start=72, end=198].
- ⚠️ Action 'Action_None' range [69-200] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [72-185] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [187-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [72-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [190-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [72-198] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-200] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-199] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-17] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-100] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-17] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-17] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-195] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-200] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-97] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>