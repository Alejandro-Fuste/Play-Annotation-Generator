# Play-Annotation-Generator Annotation Review — Counter_292

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_292`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `7` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 54 | START | 54 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `14` | 57 | START | 57 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `2` | `1` | 57 | START | 57 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `20` | `19` | 57 | START | 57 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | FB | `7` | `6` | 57 | START | 57 | 84 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 65 | END | 54 | 65 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 86 | START | 86 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `15` | 101 | START | 101 | 128 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 152 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_None` | 66 | 85 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 100 | 15 | inferred_complete_timeline |
| `Action_None` | 101 | 155 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 128 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 163 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 57 | 84 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 86 | 99 | 14 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 102 | 152 | 51 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 65 | 12 | inferred_complete_timeline |
| `Action_None` | 68 | 75 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 122 | 69 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 72 | 109 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 149 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_DownBlock` | 57 | 137 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 144 | 6 | inferred_complete_timeline |
| `Action_None` | 158 | 237 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_BallSnap` | 54 | 64 | 11 | inferred_complete_timeline |
| `Action_None` | 68 | 86 | 19 | inferred_complete_timeline |
| `Action_None` | 93 | 108 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 161 | 41 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 20 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 56 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 57 | 79 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 82 | 93 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 152 | 56 | inferred_complete_timeline |
| `Action_None` | 153 | 203 | 51 | inferred_complete_timeline |
| `Action_None` | 209 | 267 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 78 | 25 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 104 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 114 | 61 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 182 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–252
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 142 | 89 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 217 | 252 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 167 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 165 | 112 | inferred_complete_timeline |
| `Action_None` | 167 | 268 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 84 | 31 | inferred_complete_timeline |
| `Action_None` | 87 | 143 | 57 | inferred_complete_timeline |
| `Action_None` | 146 | 168 | 23 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |
| `Action_None` | 182 | 191 | 10 | inferred_complete_timeline |
| `Action_None` | 198 | 249 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 299 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 172 | 119 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 299 | 246 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_None` | 54 | 299 | 246 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `23` | Position_Unknown | Team_Unknown | 79–92 | 14 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 88–179 | 80 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 90–160 | 17 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 99–291 | 168 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 106–262 | 129 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 108–299 | 188 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 124–271 | 148 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 137–280 | 144 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 155–176 | 10 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 164–264 | 101 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 175–190 | 13 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 254–263 | 10 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (LG) duration 96 frames exceeds threshold 90 frames [start=57, end=152].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (LT) duration 93 frames exceeds threshold 90 frames [start=57, end=149].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '19' (RG) duration 96 frames exceeds threshold 90 frames [start=57, end=152].
- ⚠️ Action 'Action_None' range [54-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [57-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-144] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-237] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [57-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [86-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-122] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-252] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-167] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-249] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [57-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [72-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [130-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [151-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [54-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-108] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [57-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [82-93] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-203] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-267] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-179] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-257] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-287] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-162] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-262] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-151] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-218] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-271] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-280] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-264] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-263] for track '31' has 2 frames without a visible bounding box.
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