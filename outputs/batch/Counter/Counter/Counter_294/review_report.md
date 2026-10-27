# Play-Annotation-Generator Annotation Review — Counter_294

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_294`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 105
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | LB1 | defense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 17 | START | 17 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 20 | START | 34 | 37 |
| ✅ EXACT | `Action_DownBlock` | LG | `6` | `5` | 20 | START | 20 | 105 |
| ✅ EXACT | `Action_DownBlock` | RT | `8` | `7` | 20 | START | 20 | 105 |
| ✅ EXACT | `Action_PullBlock` | LB1 | `1` | `0` | 20 | START | 20 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 20 | START | 20 | 51 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `9` | `8` | 29 | START | 29 | 55 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 33 | END | 17 | 33 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 43 | START | 43 | 56 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `9` | `8` | 57 | START | 58 | 174 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 105 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 33 | 17 | inferred_complete_timeline |
| `Action_None` | 34 | 42 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 43 | 56 | 14 | inferred_complete_timeline |
| `Action_None` | 57 | 100 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 29 | 55 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 174 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 20 | 51 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 53 | 101 | 49 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 149 | 44 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 169 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 58 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 20 | 105 | 86 | inferred_complete_timeline |
| `Action_None` | 106 | 138 | 33 | inferred_complete_timeline |
| `Action_None` | 142 | 251 | 110 | inferred_complete_timeline |
| `Action_None` | 253 | 260 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 33 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 40 | 105 | 66 | inferred_complete_timeline |
| `Action_None` | 106 | 150 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 44 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 20 | 105 | 86 | inferred_complete_timeline |
| `Action_None` | 106 | 133 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 45 | 29 | inferred_complete_timeline |
| `Action_None` | 57 | 95 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 248 | 232 | inferred_complete_timeline |
| `Action_None` | 250 | 267 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–62
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 34 | 18 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 53 | 13 | inferred_complete_timeline |
| `Action_None` | 60 | 62 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 39 | 23 | inferred_complete_timeline |
| `Action_None` | 49 | 119 | 71 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PullBlock` | 20 | 105 | 86 | inferred_complete_timeline |
| `Action_None` | 106 | 141 | 36 | inferred_complete_timeline |
| `Action_None` | 149 | 155 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 110 | 94 | inferred_complete_timeline |
| `Action_None` | 120 | 184 | 65 | inferred_complete_timeline |
| `Action_None` | 192 | 254 | 63 | inferred_complete_timeline |
| `Action_None` | 256 | 269 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 44 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 17–158 | 140 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 57–269 | 210 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 58–146 | 84 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 72–78 | 7 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 95–269 | 175 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 104–109 | 5 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 111–217 | 99 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 113–155 | 43 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 157–160 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 161–269 | 109 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 172–176 | 5 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 176–195 | 20 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 206–269 | 64 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 208–261 | 54 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 213–269 | 51 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 225–269 | 45 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 237–269 | 33 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 249–269 | 21 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 256–269 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (3 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `9` (RB): Annotated start 57 != Inferred start 58

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [17–33], lower_priority='Action_DownBlock' annotated_start=20, effective_Action_DownBlock_start=34.
- ⚠️ Action 'Action_PullBlock' range [20-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-184] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-45] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-95] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [20-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [53-101] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-169] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-58] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [20-105] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-251] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-267] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [20-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [29-55] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-174] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [34-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [40-105] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-34] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-119] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-44] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-96] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-217] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-261] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-269] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>