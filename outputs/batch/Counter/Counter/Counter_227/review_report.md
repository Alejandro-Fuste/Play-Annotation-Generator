# Play-Annotation-Generator Annotation Review — Counter_227

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_227`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 45 | START | 45 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 48 | START | 61 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `22` | `21` | 48 | START | 48 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `9` | `8` | 48 | START | 48 | 102 |
| ✅ EXACT | `Action_PullBlock` | LG | `12` | `11` | 48 | START | 48 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE1 | `2` | `1` | 48 | START | 48 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | QB | `7` | `6` | 53 | START | 53 | 81 |
| ✅ EXACT | `Action_SnapReceive` | RB | `11` | `10` | 60 | END | 45 | 60 |
| ✅ EXACT | `Action_Handoff` | RB | `11` | `10` | 75 | START | 75 | 95 |
| ✅ EXACT | `Action_BallCarry` | QB | `7` | `6` | 96 | START | 96 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 131 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 53 | 81 | 29 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 86 | 95 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 96 | 179 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_None` | 61 | 74 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 75 | 95 | 21 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 239 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 212 | 168 | inferred_complete_timeline |
| `Action_None` | 215 | 227 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 48 | 95 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 129 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 161 | 117 | inferred_complete_timeline |
| `Action_None` | 163 | 184 | 22 | inferred_complete_timeline |
| `Action_None` | 186 | 195 | 10 | inferred_complete_timeline |
| `Action_None` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 67 | 23 | inferred_complete_timeline |
| `Action_None` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 180 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 48 | 131 | 84 | inferred_complete_timeline |
| `Action_None` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 61 | 131 | 71 | inferred_complete_timeline |
| `Action_None` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 108 | 61 | inferred_complete_timeline |
| `Action_DownBlock` | 112 | 131 | 20 | inferred_complete_timeline |
| `Action_None` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 48 | 102 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 131 | 24 | inferred_complete_timeline |
| `Action_None` | 132 | 151 | 20 | inferred_complete_timeline |
| `Action_None` | 153 | 239 | 87 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 122 | 78 | inferred_complete_timeline |
| `Action_None` | 125 | 239 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 114 | 70 | inferred_complete_timeline |
| `Action_None` | 121 | 173 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 66 | 22 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 136 | 92 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 230 | 186 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 175 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_None` | 45 | 233 | 189 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `32` | Position_Unknown | Team_Unknown | 108–239 | 131 | 2 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 108–191 | 25 | 3 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 128–133 | 4 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 141–239 | 63 | 2 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 166–239 | 74 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 170–174 | 5 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 178–239 | 60 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 178–239 | 56 | 4 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 203–239 | 27 | 3 | Undefined position; Undefined team |
| `34` | `54` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 234–239 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [45–60], lower_priority='Action_DownBlock' annotated_start=48, effective_Action_DownBlock_start=61.
- ⚠️ Action 'Action_None' range [45-212] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-227] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [48-95] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [97-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-175] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-184] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-88] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-180] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [53-81] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [83-84] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [96-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-239] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-66] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-230] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-233] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-136] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [61-131] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [48-108] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-239] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-123] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-184] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-207] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-223] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-236] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-209] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '35' has 2 frames without a visible bounding box.
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