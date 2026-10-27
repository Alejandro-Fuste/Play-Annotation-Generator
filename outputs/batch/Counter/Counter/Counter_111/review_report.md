# Play-Annotation-Generator Annotation Review — Counter_111

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_111`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | WR3 | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `19` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 46 | START | 46 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `2` | 50 | START | 50 | 97 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `7` | `6` | 50 | START | 50 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | TE | `14` | `13` | 52 | START | 52 | 111 |
| ✅ EXACT | `Action_DownBlock` | LT | `18` | `17` | 52 | START | 52 | 161 |
| ✅ EXACT | `Action_DownBlock` | LG | `22` | `21` | 52 | START | 52 | 73 |
| ✅ EXACT | `Action_SnapReceive` | WR3 | `9` | `8` | 62 | END | 46 | 62 |
| ✅ EXACT | `Action_BallCarry` | QB | `19` | `18` | 79 | START | 79 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 161 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 269 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 122 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 112 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 269 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 111 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 161 | 48 | inferred_complete_timeline |
| `Action_None` | 162 | 186 | 25 | inferred_complete_timeline |
| `Action_None` | 197 | 269 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 161 | 110 | inferred_complete_timeline |
| `Action_None` | 162 | 269 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 73 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 94 | 32 | inferred_complete_timeline |
| `Action_None` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_None` | 120 | 157 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 50 | 97 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 103 | 106 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 72 | 27 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 97 | 52 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 90 | 45 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 189 | 144 | inferred_complete_timeline |
| `Action_None` | 191 | 205 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 187 | 142 | inferred_complete_timeline |
| `Action_None` | 190 | 215 | 26 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 236 | 8 | inferred_complete_timeline |
| `Action_None` | 247 | 249 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 167 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 79 | 34 | inferred_complete_timeline |
| `Action_None` | 81 | 89 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 269 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 168 | 123 | inferred_complete_timeline |
| `Action_None` | 184 | 260 | 77 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 185 | 140 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 209 | 164 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 247 | 25 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–269 | 265 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 81–269 | 185 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 92–269 | 167 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 130–157 | 28 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 140–269 | 130 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 149–269 | 112 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 154–269 | 116 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 171–269 | 99 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 172–269 | 98 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 177–269 | 93 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 184–269 | 86 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 215–269 | 50 | 3 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 224: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (TE) duration 110 frames exceeds threshold 90 frames [start=52, end=161].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (LT) duration 110 frames exceeds threshold 90 frames [start=52, end=161].
- ⚠️ Action 'Action_None' range [46-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [50-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [103-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-205] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-215] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [50-158] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-97] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-111] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-186] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-247] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-260] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-161] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [52-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-109] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-109] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-242] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-231] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>