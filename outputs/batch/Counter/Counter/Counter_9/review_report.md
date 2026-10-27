# Play-Annotation-Generator Annotation Review — Counter_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_9`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `18` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 49 | START | 49 | 64 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | TE | `3` | `2` | 56 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | LG | `14` | `13` | 56 | START | 56 | 151 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `3` | `2` | 56 | START | 56 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 64 | END | 49 | 64 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 78 | START | 78 | 94 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `5` | `4` | 95 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 151 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_SnapReceive` | 49 | 64 | 16 | inferred_complete_timeline |
| `Action_None` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 126 | 78 | inferred_complete_timeline |
| `Action_None` | 130 | 299 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 238 | 190 | inferred_complete_timeline |
| `Action_None` | 240 | 271 | 32 | inferred_complete_timeline |
| `Action_None` | 273 | 299 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 56 | 151 | 96 | inferred_complete_timeline |
| `Action_None` | 152 | 254 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 136 | 88 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PullBlock` | 56 | 151 | 96 | inferred_complete_timeline |
| `Action_None` | 152 | 228 | 77 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 49 | 64 | 16 | inferred_complete_timeline |
| `Action_None` | 65 | 100 | 36 | inferred_complete_timeline |
| `Action_None` | 122 | 240 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–132
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 62 | 14 | inferred_complete_timeline |
| `Action_None` | 73 | 132 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 69 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 179 | 131 | inferred_complete_timeline |
| `Action_None` | 193 | 299 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 98 | 50 | inferred_complete_timeline |
| `Action_None` | 100 | 299 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 71 | 23 | inferred_complete_timeline |
| `Action_None` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 84 | 117 | 34 | inferred_complete_timeline |
| `Action_None` | 130 | 235 | 106 | inferred_complete_timeline |
| `Action_None` | 238 | 247 | 10 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 122 | 74 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 164 | 31 | inferred_complete_timeline |
| `Action_None` | 174 | 177 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 299 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 156 | 108 | inferred_complete_timeline |
| `Action_None` | 158 | 175 | 18 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 202 | 19 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 203 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 292 | 244 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 299 | 251 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 2–299 | 297 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 4–14 | 11 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 90–299 | 197 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 108–299 | 178 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 155–299 | 122 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 188–214 | 10 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 201–206 | 6 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 205–209 | 5 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 224–299 | 76 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 232–235 | 4 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 241–264 | 16 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 264–283 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `3` (TE)
- ❌ Missing segment for action `Action_BallCarry` on target `5` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF3` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 56 for track '2': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Segment 'Action_BallCarry' for track '4' has invalid range: start=95, end=84. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '13' (LG) duration 96 frames exceeds threshold 90 frames [start=56, end=151].
- ⚠️ Action 'Action_None' range [49-179] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-235] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-240] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-126] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-228] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-202] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-238] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-271] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-62] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-14] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-288] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-299] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-283] for track '33' has 3 frames without a visible bounding box.
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

</details>