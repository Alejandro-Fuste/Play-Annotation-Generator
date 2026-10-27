# Play-Annotation-Generator Annotation Review — Counter_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_8`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | LB2 | defense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 85 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `16` | `15` | 82 | START | N/A | N/A |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 86 | START | 86 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `2` | `1` | 86 | START | 86 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `8` | `7` | 86 | START | 86 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | LB2 | `1` | `0` | 86 | START | 86 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `16` | `15` | 86 | START | 88 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RB | `4` | `3` | 86 | START | 86 | 116 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 86 | END | 82 | 86 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 117 | START | 117 | 129 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 130 | START | 130 | 167 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 176 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_SnapReceive` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_None` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 116 | 26 | inferred_complete_timeline |
| `Action_Handoff` | 117 | 129 | 13 | inferred_complete_timeline |
| `Action_None` | 130 | 163 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 86 | 116 | 31 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 119 | 129 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 167 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 32 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 110 | 29 | inferred_complete_timeline |
| `Action_None` | 116 | 145 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 81 | 75 | inferred_complete_timeline |
| `Action_None` | 82 | 177 | 96 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 107 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 131 | 46 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 176 | 23 | inferred_complete_timeline |
| `Action_None` | 177 | 177 | 1 | inferred_complete_timeline |
| `Action_None` | 181 | 204 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 114 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 117 | 170 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_None` | 177 | 193 | 17 | inferred_complete_timeline |
| `Action_None` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 108 | 27 | inferred_complete_timeline |
| `Action_None` | 111 | 112 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 225 | 144 | inferred_complete_timeline |
| `Action_None` | 229 | 269 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 152 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 142 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 134 | 53 | inferred_complete_timeline |
| `Action_None` | 140 | 175 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 141 | 60 | inferred_complete_timeline |
| `Action_None` | 147 | 188 | 42 | inferred_complete_timeline |
| `Action_None` | 191 | 269 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 86 | 175 | 90 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 177 | 213 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 82 | 269 | 188 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 88–269 | 169 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 90–269 | 180 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 115–256 | 102 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 115–207 | 83 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 130–143 | 14 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 152–154 | 3 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 153–202 | 49 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 158–269 | 99 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 159–269 | 111 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 163–170 | 7 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 170–200 | 31 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 170–196 | 26 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 190–269 | 77 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 193–200 | 8 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 224–269 | 46 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 238–269 | 28 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 240–269 | 30 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 259–261 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `16` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (LG) duration 91 frames exceeds threshold 90 frames [start=86, end=176].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (RG) duration 91 frames exceeds threshold 90 frames [start=86, end=176].
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=88, end=86. Clamping end to start.
- ⚠️ Action 'Action_PlaySideFakeStep' range [86-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [177-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-131] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '1' starts at frame 177, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [177-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [86-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-225] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [117-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-193] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-152] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-175] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-110] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-145] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [88-143] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [149-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-143] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-193] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-207] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '32' has 1 frames without a visible bounding box.
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

</details>