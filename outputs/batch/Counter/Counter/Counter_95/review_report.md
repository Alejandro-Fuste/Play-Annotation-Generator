# Play-Annotation-Generator Annotation Review — Counter_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_95`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `17` | `16` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 8 | START | 8 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 8 | START | 8 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 8 | START | 8 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 8 | START | 8 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 8 | START | 8 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 8 | START | 8 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 8 | START | 8 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 8 | START | 8 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `22` | `Group` | 8 | START | 8 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 8 | START | 8 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 8 | START | 8 | 100 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 101 | START | 101 | 115 |
| ✅ EXACT | `Action_DownBlock` | LG | `19` | `18` | 108 | START | 108 | 121 |
| ✅ EXACT | `Action_DownBlock` | LG | `19` | `18` | 108 | START | 108 | 121 |
| ✅ EXACT | `Action_PullBlock` | RG | `17` | `16` | 108 | START | 108 | 206 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `10` | `9` | 108 | START | 108 | 195 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `18` | `17` | 115 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | C | `18` | `17` | 125 | START | 125 | 137 |
| ✅ EXACT | `Action_BallCarry` | QB | `3` | `2` | 144 | START | 144 | 269 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 206 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 143 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 269 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–206
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 182 | 82 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 8–269
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 139 | 39 | inferred_complete_timeline |
| `Action_None` | 205 | 269 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–121
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 107 | 100 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 121 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 8–190
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_BallSnap` | 101 | 115 | 15 | inferred_complete_timeline |
| `Action_None` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 125 | 137 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 161 | 18 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 190 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 8–226
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 107 | 100 | inferred_complete_timeline |
| `Action_PullBlock` | 108 | 206 | 99 | inferred_complete_timeline |
| `Action_None` | 207 | 226 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–195
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 107 | 100 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 195 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–263
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 263 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–238
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 159 | 59 | inferred_complete_timeline |
| `Action_None` | 165 | 238 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–144
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 144 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–209
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 209 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 269 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–158
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 100 | 93 | inferred_complete_timeline |
| `Action_None` | 101 | 158 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 8–184 | 176 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 120–269 | 88 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 141–269 | 117 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 143–269 | 127 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 171–268 | 75 | 6 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 202–269 | 65 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 204–212 | 9 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 206–269 | 63 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 229–269 | 41 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 230–269 | 24 | 5 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 242–253 | 12 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 253–269 | 12 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 259–262 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `18` (C)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (RG) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
- ⚠️ Segment 'Action_DownBlock' for track '17' has invalid range: start=108, end=100. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [101–115], lower_priority='Action_DownBlock' annotated_start=108, effective_Action_DownBlock_start=116.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [101–115], lower_priority='Action_SnapReceive' annotated_start=101, effective_Action_SnapReceive_start=116.
- ⚠️ Action 'Action_None' range [101-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-238] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-269] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [125-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-190] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-184] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-245] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-231] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-240] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>