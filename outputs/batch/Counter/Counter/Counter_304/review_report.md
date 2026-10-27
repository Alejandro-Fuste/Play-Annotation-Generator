# Play-Annotation-Generator Annotation Review — Counter_304

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_304`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 66
- **Validation Warnings:** 56
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 78 | START | 78 | 90 |
| ✅ EXACT | `Action_DownBlock` | LT | `11` | `10` | 81 | START | 81 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 81 | START | 91 | 155 |
| ✅ EXACT | `Action_DownBlock` | LG | `14` | `13` | 81 | START | 81 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `12` | `11` | 81 | START | 81 | 91 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `3` | `2` | 81 | START | 81 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 90 | END | 78 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `15` | `14` | 91 | START | 91 | 123 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 99 | START | 99 | 126 |
| ✅ EXACT | `Action_BallCarry` | RB | `15` | `14` | 129 | START | 129 | 163 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 90 | 13 | inferred_complete_timeline |
| `Action_None` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 99 | 126 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 91 | 123 | 33 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 163 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 81 | 104 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 155 | 75 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 138 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 90 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 155 | 65 | inferred_complete_timeline |
| `Action_None` | 156 | 161 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PullBlock` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 110 | 116 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 126 | 140 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 149 | 151 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 157 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 130 | 53 | inferred_complete_timeline |
| `Action_None` | 133 | 239 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 153 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 134 | 57 | inferred_complete_timeline |
| `Action_None` | 139 | 185 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 164 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 217 | 140 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 141 | 64 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 154 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 239 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 98–239 | 137 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 119–128 | 10 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 139–174 | 33 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 153–225 | 73 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 156–239 | 84 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 163–238 | 71 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 200–239 | 40 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 204–239 | 31 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 27 | 76 | 24 | 48.0% | 32–40, 52, 58–59, 62–75 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [78–90], lower_priority='Action_DownBlock' annotated_start=81, effective_Action_DownBlock_start=91.
- ⚠️ Action 'Action_None' range [78-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-154] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [81-104] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-130] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-164] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-185] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-217] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [81-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [110-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [126-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [144-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [149-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-138] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [91-123] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [99-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-106] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-155] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-225] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-227] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '25' has 1 frames without a visible bounding box.
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

</details>