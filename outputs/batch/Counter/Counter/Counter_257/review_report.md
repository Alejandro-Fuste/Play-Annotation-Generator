# Play-Annotation-Generator Annotation Review — Counter_257

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_257`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `16` | `15` |
| ✅ EXACT | `Action_DownBlock` | TE2 | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `20` | `19` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 74 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 75 | START | 75 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `12` | `11` | 78 | START | 80 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `16` | `15` | 78 | START | 78 | 106 |
| ✅ EXACT | `Action_DownBlock` | TE2 | `5` | `4` | 78 | START | 78 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `22` | `21` | 78 | START | 89 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `20` | `19` | 78 | START | 88 | 94 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 79 | END | 75 | 79 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `18` | 104 | START | 104 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 120 | START | 120 | 129 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–272
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 50 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 74 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_None` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_None` | 82 | 103 | 22 | inferred_complete_timeline |
| `Action_Handoff` | 104 | 119 | 16 | inferred_complete_timeline |
| `Action_None` | 120 | 272 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 129 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 140 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 232 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 299 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 149 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 100 | 122 | 23 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 124 | 146 | 23 | inferred_complete_timeline |
| `Action_None` | 147 | 299 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 146 | 69 | inferred_complete_timeline |
| `Action_None` | 147 | 159 | 13 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 69 | 14 | inferred_complete_timeline |
| `Action_None` | 84 | 129 | 46 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 272 | 127 | inferred_complete_timeline |
| `Action_None` | 274 | 299 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_BallSnap` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 80 | 139 | 60 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 146 | 1 | inferred_complete_timeline |
| `Action_None` | 147 | 151 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 74 | 45 | inferred_complete_timeline |
| `Action_None` | 75 | 98 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_DownBlock` | 78 | 106 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 74 | 19 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 107 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 159 | 85 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 72 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 74 | 1 | inferred_complete_timeline |
| `Action_None` | 75 | 79 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 117 | 36 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 38 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 48 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_None` | 75 | 122 | 48 | inferred_complete_timeline |
| `Action_None` | 125 | 141 | 17 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_None` | 164 | 299 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 161 | 80 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 156 | 82 | inferred_complete_timeline |
| `Action_None` | 163 | 299 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 242 | 168 | inferred_complete_timeline |
| `Action_None` | 246 | 289 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 126 | 52 | inferred_complete_timeline |
| `Action_None` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 147 | 160 | 14 | inferred_complete_timeline |
| `Action_None` | 163 | 181 | 19 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 196 | 7 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 299 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 160 | 86 | inferred_complete_timeline |
| `Action_None` | 163 | 173 | 11 | inferred_complete_timeline |
| `Action_None` | 178 | 299 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 299 | 225 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 3–267 | 193 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 106–299 | 178 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 111–117 | 7 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 118–299 | 132 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 148–171 | 14 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 164–253 | 90 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 167–299 | 114 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 176–299 | 113 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 238–270 | 33 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 260–262 | 3 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 274–299 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 87 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [75–79], lower_priority='Action_DownBlock' annotated_start=78, effective_Action_DownBlock_start=80.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-48] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-232] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-149] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-146] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-181] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-161] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-156] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-160] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [80-139] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [142-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-72] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-79] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-289] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [78-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-41] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 80, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [80-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [104-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-272] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [88-94] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [100-122] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [124-146] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-272] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-10] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [89-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-144] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-160] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-299] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-270] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '31' has 1 frames without a visible bounding box.
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