# Play-Annotation-Generator Annotation Review — Counter_251

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_251`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `28` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `19` | `14` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | offense | `24` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `20` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | offense | `28` | `19` |
| ⚠️ END CHANGED | `Action_SnapReceive` | RG | offense | `24` | `16` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | CB1 | defense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 24 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 33 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `24` | `Group` | 0 | START | 39 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `28` | `Group` | 0 | START | 43 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 100 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 73 | START | 73 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 76 | START | 89 | 90 |
| ✅ EXACT | `Action_DownBlock` | RT | `19` | `14` | 76 | START | 76 | 88 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | `24` | `16` | 76 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `20` | `15` | 76 | START | 76 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE2 | `28` | `19` | 76 | START | 76 | 84 |
| ⚠️ END CHANGED | `Action_SnapReceive` | RG | `24` | `16` | 88 | END | 73 | 84 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 101 | START | 101 | 113 |
| ✅ EXACT | `Action_BallCarry` | CB1 | `5` | `4` | 114 | START | 114 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 147 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_Handoff` | 101 | 113 | 13 | inferred_complete_timeline |
| `Action_None` | 114 | 156 | 43 | inferred_complete_timeline |
| `Action_None` | 162 | 239 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 220 | 148 | inferred_complete_timeline |
| `Action_None` | 223 | 228 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 187 | 115 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `28`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `28`
- **team_side:** `offense`
- **Visible Frames:** 43–239
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 43 | 75 | 33 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 87 | 129 | 43 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 133 | 147 | 15 | inferred_complete_timeline |
| `Action_None` | 148 | 239 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 33–221
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 33 | 75 | 43 | inferred_complete_timeline |
| `Action_PullBlock` | 76 | 133 | 58 | inferred_complete_timeline |
| `Action_PullBlock` | 137 | 147 | 11 | inferred_complete_timeline |
| `Action_None` | 148 | 204 | 57 | inferred_complete_timeline |
| `Action_None` | 207 | 221 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallSnap` | 73 | 88 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 127 | 147 | 21 | inferred_complete_timeline |
| `Action_None` | 148 | 239 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `24`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 39–239
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 72 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 84 | 12 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 24–88
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 75 | 52 | inferred_complete_timeline |
| `Action_DownBlock` | 76 | 88 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 115 | 43 | inferred_complete_timeline |
| `Action_None` | 120 | 130 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `29`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `29`
- **team_side:** `defense`
- **Visible Frames:** 44–239
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 44 | 72 | 29 | inferred_complete_timeline |
| `Action_None` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 144 | 30 | inferred_complete_timeline |
| `Action_None` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `25`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 39–239
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 39 | 72 | 34 | inferred_complete_timeline |
| `Action_None` | 73 | 83 | 11 | inferred_complete_timeline |
| `Action_None` | 98 | 114 | 17 | inferred_complete_timeline |
| `Action_None` | 118 | 230 | 113 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 232 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 90 | 95 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 131 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 239 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 130 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_None` | 73 | 233 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `27` | Position_Unknown | Team_Unknown | 41–239 | 198 | 3 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 88–239 | 118 | 3 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 117–237 | 121 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 125–141 | 17 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 151–239 | 89 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 155–239 | 81 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 169–234 | 62 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `24` (RG)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `28` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 504: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [73–88], lower_priority='Action_DownBlock' annotated_start=76, effective_Action_DownBlock_start=89.
- ⚠️ Segment 'Action_DownBlock' for track '16' has invalid range: start=76, end=72. Clamping end to start.
- ⚠️ Action 'Action_None' range [73-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-239] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-130] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-232] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-131] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [89-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-239] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [76-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [76-133] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [73-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-239] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-83] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-230] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-59] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [76-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [87-129] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-141] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>