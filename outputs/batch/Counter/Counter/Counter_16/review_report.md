# Play-Annotation-Generator Annotation Review — Counter_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_16`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF | defense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 18 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 19 | START | 19 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 25 | START | 35 | 96 |
| ✅ EXACT | `Action_DownBlock` | RT | `2` | `1` | 25 | START | 25 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `4` | 25 | START | 25 | 53 |
| ✅ EXACT | `Action_PullBlock` | LG | `12` | `11` | 25 | START | 25 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | SAF | `11` | `10` | 25 | START | 25 | 47 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 34 | END | 19 | 34 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `5` | 45 | START | 45 | 72 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 73 | START | 73 | 184 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 129 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 34 | 16 | inferred_complete_timeline |
| `Action_None` | 35 | 44 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 45 | 72 | 28 | inferred_complete_timeline |
| `Action_None` | 73 | 191 | 119 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 184 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 121 | 103 | inferred_complete_timeline |
| `Action_None` | 127 | 239 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 41 | 23 | inferred_complete_timeline |
| `Action_None` | 47 | 57 | 11 | inferred_complete_timeline |
| `Action_None` | 60 | 166 | 107 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 25 | 129 | 105 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 34 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 35 | 96 | 62 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 129 | 23 | inferred_complete_timeline |
| `Action_None` | 130 | 155 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 25 | 53 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 57 | 129 | 73 | inferred_complete_timeline |
| `Action_None` | 130 | 181 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 25 | 129 | 105 | inferred_complete_timeline |
| `Action_None` | 130 | 138 | 9 | inferred_complete_timeline |
| `Action_None` | 140 | 153 | 14 | inferred_complete_timeline |
| `Action_None` | 157 | 168 | 12 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 165 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 108 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 43 | 25 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 37 | 19 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_None` | 49 | 79 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 109 | 28 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 86 | 68 | inferred_complete_timeline |
| `Action_None` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_None` | 100 | 143 | 44 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 74 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–212
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 107 | 89 | inferred_complete_timeline |
| `Action_None` | 117 | 212 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 25 | 47 | 23 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 52 | 124 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 20–75 | 55 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 68–137 | 67 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 71–239 | 166 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 83–94 | 12 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 97–131 | 35 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 114–239 | 126 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 125–140 | 16 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 140–239 | 96 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 145–167 | 23 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 152–239 | 88 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 157–239 | 83 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 196–234 | 21 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 200–213 | 13 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 210–239 | 10 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (RT) duration 105 frames exceeds threshold 90 frames [start=25, end=129].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (RG) duration 105 frames exceeds threshold 90 frames [start=25, end=129].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (LG) duration 105 frames exceeds threshold 90 frames [start=25, end=129].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 105 frames exceeds threshold 90 frames [start=25, end=129].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [19–34], lower_priority='Action_DownBlock' annotated_start=25, effective_Action_DownBlock_start=35.
- ⚠️ Action 'Action_None' range [19-121] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-153] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '3' starts at frame 73, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [73-184] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [25-53] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-166] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-212] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [25-47] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [52-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [25-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-143] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [35-96] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-37] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-46] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-79] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-109] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-54] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-217] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-94] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-131] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-228] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-216] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-213] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '30' has 1 frames without a visible bounding box.
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