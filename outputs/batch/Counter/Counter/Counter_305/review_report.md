# Play-Annotation-Generator Annotation Review — Counter_305

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_305`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 41 | START | 41 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `18` | `17` | 44 | START | 56 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `21` | `20` | 44 | START | 44 | 50 |
| ✅ EXACT | `Action_PullBlock` | LG | `19` | `18` | 44 | START | 44 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `22` | `21` | 44 | START | 44 | 45 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 55 | END | 41 | 55 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 65 | START | 65 | 89 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 90 | START | 90 | 230 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 139 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 55 | 15 | inferred_complete_timeline |
| `Action_None` | 56 | 64 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 65 | 89 | 25 | inferred_complete_timeline |
| `Action_None` | 90 | 273 | 184 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 89 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 90 | 230 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 209 | 169 | inferred_complete_timeline |
| `Action_None` | 212 | 243 | 32 | inferred_complete_timeline |
| `Action_None` | 245 | 251 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 241 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 62 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 74 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 124 | 22 | inferred_complete_timeline |
| `Action_None` | 126 | 152 | 27 | inferred_complete_timeline |
| `Action_None` | 155 | 166 | 12 | inferred_complete_timeline |
| `Action_None` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 126 | 86 | inferred_complete_timeline |
| `Action_None` | 128 | 184 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 12 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 21 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 49 | 112 | 64 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 129 | 139 | 11 | inferred_complete_timeline |
| `Action_None` | 140 | 215 | 76 | inferred_complete_timeline |
| `Action_None` | 217 | 224 | 8 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PullBlock` | 44 | 139 | 96 | inferred_complete_timeline |
| `Action_None` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 158 | 166 | 9 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 104 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 139 | 27 | inferred_complete_timeline |
| `Action_None` | 140 | 252 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_DownBlock` | 44 | 50 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 133 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 139 | 5 | inferred_complete_timeline |
| `Action_None` | 140 | 144 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 193 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 86 | 46 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 193 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 77 | 37 | inferred_complete_timeline |
| `Action_None` | 79 | 135 | 57 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 299 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 71 | 31 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 133 | 93 | inferred_complete_timeline |
| `Action_None` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_None` | 149 | 196 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 113 | 73 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_None` | 137 | 244 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 101 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 243 | 203 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 246 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 235 | 195 | inferred_complete_timeline |
| `Action_None` | 240 | 266 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 299 | 259 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 98–182 | 31 | 8 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 107–227 | 115 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 119–122 | 4 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 142–181 | 40 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 163–185 | 23 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 211–213 | 3 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `22` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (C) duration 96 frames exceeds threshold 90 frames [start=44, end=139].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [41–55], lower_priority='Action_DownBlock' annotated_start=44, effective_Action_DownBlock_start=56.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '18' (LG) duration 96 frames exceeds threshold 90 frames [start=44, end=139].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 96 frames exceeds threshold 90 frames [start=44, end=139].
- ⚠️ Action 'Action_None' range [41-209] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-246] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-241] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-193] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [90-230] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-266] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-244] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-273] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-135] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-62] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [41-51] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [56-57] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-64] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [106-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-139] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-252] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [44-139] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-126] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [44-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 140, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [140-144] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-21] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [44-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [49-112] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [118-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-215] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-224] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-164] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-181] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-185] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-299] for track '28' has 1 frames without a visible bounding box.
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