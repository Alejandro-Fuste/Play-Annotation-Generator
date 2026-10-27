# Play-Annotation-Generator Annotation Review — Counter_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_82`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 23 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `6` | `5` | 24 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | LG | `14` | `13` | 24 | START | 24 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `6` | `5` | 24 | START | 24 | 46 |
| ✅ EXACT | `Action_DownBlock` | LT | `7` | `6` | 24 | START | 24 | 95 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `13` | `12` | 24 | START | 24 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `1` | `0` | 24 | START | 24 | 85 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `3` | `2` | 24 | START | 24 | 95 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 38 | END | 24 | 38 |
| ✅ EXACT | `Action_Handoff` | QB | `4` | `3` | 45 | START | 45 | 56 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `12` | 57 | START | 57 | 151 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 95 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 39 | 44 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_None` | 57 | 111 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 24 | 56 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 57 | 151 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 95 | 72 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 24 | 46 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 24 | 85 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 97 | 299 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 290 | 267 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 294 | 271 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 78 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 42 | 19 | inferred_complete_timeline |
| `Action_None` | 45 | 58 | 14 | inferred_complete_timeline |
| `Action_None` | 60 | 232 | 173 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 249 | 256 | 8 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 31 | 8 | inferred_complete_timeline |
| `Action_None` | 35 | 46 | 12 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 53 | 64 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 39 | 16 | inferred_complete_timeline |
| `Action_None` | 43 | 299 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 299 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 110 | 87 | inferred_complete_timeline |
| `Action_None` | 112 | 185 | 74 | inferred_complete_timeline |
| `Action_None` | 187 | 299 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 119 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 103 | 80 | inferred_complete_timeline |
| `Action_None` | 105 | 285 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `20` | Position_Unknown | Team_Unknown | 47–299 | 251 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 60–299 | 240 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 73–299 | 226 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 91–94 | 4 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 112–187 | 76 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 117–299 | 183 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 123–299 | 157 | 5 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 135–138 | 4 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 141–151 | 8 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 164–299 | 136 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 172–299 | 128 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 187–299 | 111 | 2 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 266–269 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `6` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 24 for track '5': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
- ⚠️ Action 'Action_PullBlock' range [24-85] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [87-94] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [24-95] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [45-56] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [24-46] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-294] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-285] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-119] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [57-151] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [24-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-31] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-58] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-256] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-76] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-253] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-187] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-153] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-299] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-287] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '30' has 1 frames without a visible bounding box.
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

</details>