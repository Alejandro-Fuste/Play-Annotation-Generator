# Play-Annotation-Generator Annotation Review — Counter_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_51`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | FB | offense | `16` | `15` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_BallCarry` | DT2 | defense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `16` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 98 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 99 | START | 99 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 107 | START | 115 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 107 | START | 107 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `21` | `20` | 107 | START | 107 | 154 |
| ✅ EXACT | `Action_PullLeadBlock` | FB | `16` | `15` | 107 | START | 107 | 154 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 112 | END | 99 | 112 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 127 | START | 127 | 138 |
| ✅ EXACT | `Action_BallCarry` | DT2 | `15` | `14` | 139 | START | 139 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 198 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 113 | 126 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 127 | 138 | 12 | inferred_complete_timeline |
| `Action_None` | 139 | 288 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 161 | 63 | inferred_complete_timeline |
| `Action_None` | 164 | 174 | 11 | inferred_complete_timeline |
| `Action_None` | 178 | 194 | 17 | inferred_complete_timeline |
| `Action_None` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 107 | 154 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 216 | 118 | inferred_complete_timeline |
| `Action_None` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 158 | 60 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 111 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 122 | 7 | inferred_complete_timeline |
| `Action_None` | 130 | 160 | 31 | inferred_complete_timeline |
| `Action_None` | 180 | 203 | 24 | inferred_complete_timeline |
| `Action_None` | 218 | 242 | 25 | inferred_complete_timeline |
| `Action_None` | 245 | 299 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 136 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 156 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 199 | 246 | 48 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 299 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 198 | 64 | inferred_complete_timeline |
| `Action_None` | 199 | 286 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 154 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 156 | 162 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 185 | 87 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 134 | 36 | inferred_complete_timeline |
| `Action_None` | 160 | 172 | 13 | inferred_complete_timeline |
| `Action_None` | 197 | 216 | 20 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 162 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 170 | 72 | inferred_complete_timeline |
| `Action_None` | 188 | 297 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 214 | 116 | inferred_complete_timeline |
| `Action_None` | 217 | 248 | 32 | inferred_complete_timeline |
| `Action_None` | 261 | 286 | 26 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 151 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 253 | 155 | inferred_complete_timeline |
| `Action_None` | 258 | 266 | 9 | inferred_complete_timeline |
| `Action_None` | 272 | 284 | 13 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–275 | 261 | 5 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 159–204 | 45 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 178–299 | 122 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 180–295 | 100 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 183–299 | 117 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 193–246 | 31 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 214–299 | 86 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 292–299 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 104: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (C) duration 92 frames exceeds threshold 90 frames [start=107, end=198].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [99–112], lower_priority='Action_DownBlock' annotated_start=107, effective_Action_DownBlock_start=113.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 92 frames exceeds threshold 90 frames [start=107, end=198].
- ⚠️ Action 'Action_None' range [99-216] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-275] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-161] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-253] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-266] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-297] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-158] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-214] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-248] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-288] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [107-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-134] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-216] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [99-112] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [123-129] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-156] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [192-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-154] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [156-162] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-160] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-203] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-242] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-171] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-242] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-280] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-299] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>