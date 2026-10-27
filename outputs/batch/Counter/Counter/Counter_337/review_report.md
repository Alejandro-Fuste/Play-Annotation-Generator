# Play-Annotation-Generator Annotation Review — Counter_337

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_337`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 46 | START | 46 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `14` | 49 | START | 60 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `16` | `15` | 49 | START | 49 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `21` | `20` | 49 | START | 49 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 49 | START | 49 | 66 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `13` | `12` | 49 | START | 49 | 155 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `11` | `10` | 53 | START | 53 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 59 | END | 46 | 59 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 72 | START | 72 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `10` | 89 | START | 89 | 259 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_None` | 60 | 71 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 72 | 88 | 17 | inferred_complete_timeline |
| `Action_None` | 89 | 299 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 53 | 88 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 259 | 171 | inferred_complete_timeline |
| `Action_BallCarry` | 261 | 272 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 185 | 140 | inferred_complete_timeline |
| `Action_None` | 190 | 245 | 56 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 99 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 49 | 97 | 49 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 110 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 131 | 155 | 25 | inferred_complete_timeline |
| `Action_None` | 156 | 244 | 89 | inferred_complete_timeline |
| `Action_None` | 269 | 299 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 59 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 105 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 155 | 43 | inferred_complete_timeline |
| `Action_None` | 156 | 281 | 126 | inferred_complete_timeline |
| `Action_None` | 283 | 290 | 8 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PullBlock` | 49 | 66 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 72 | 155 | 84 | inferred_complete_timeline |
| `Action_None` | 156 | 282 | 127 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 49 | 155 | 107 | inferred_complete_timeline |
| `Action_None` | 156 | 178 | 23 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 61 | 16 | inferred_complete_timeline |
| `Action_None` | 65 | 172 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 125 | 80 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 63 | 18 | inferred_complete_timeline |
| `Action_None` | 65 | 76 | 12 | inferred_complete_timeline |
| `Action_None` | 87 | 96 | 10 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 68 | 23 | inferred_complete_timeline |
| `Action_None` | 72 | 299 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 138 | 93 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 172 | 295 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 98 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 118 | 73 | inferred_complete_timeline |
| `Action_None` | 122 | 299 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 225 | 180 | inferred_complete_timeline |
| `Action_None` | 231 | 234 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 145 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–285 | 286 | 2 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–299 | 278 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 25–299 | 218 | 8 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 87–93 | 7 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 98–102 | 5 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 104–291 | 183 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 147–298 | 120 | 6 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 149–239 | 84 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 162–299 | 138 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 170–299 | 130 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 184–299 | 94 | 6 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 204–299 | 92 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 265–299 | 35 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 267–271 | 5 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 676: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ Row 676: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (C) duration 107 frames exceeds threshold 90 frames [start=49, end=155].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [46–59], lower_priority='Action_DownBlock' annotated_start=49, effective_Action_DownBlock_start=60.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (LG) duration 107 frames exceeds threshold 90 frames [start=49, end=155].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (RG) duration 107 frames exceeds threshold 90 frames [start=49, end=155].
- ⚠️ Action 'Action_None' range [46-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-285] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-132] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-202] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-299] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-295] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-259] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-272] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [49-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-172] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-76] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-281] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-290] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [49-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [131-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-76] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [49-66] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [72-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-282] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [49-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-28] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-76] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-159] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-291] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-249] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-286] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-230] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-282] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-243] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-271] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>