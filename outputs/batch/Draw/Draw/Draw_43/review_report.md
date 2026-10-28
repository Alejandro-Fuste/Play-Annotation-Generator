# Play-Annotation-Generator Annotation Review — Draw_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `1` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 61 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 62 | START | 62 | 76 |
| ✅ EXACT | `Action_PassBlock` | LG | `11` | `10` | 65 | START | 65 | 134 |
| ✅ EXACT | `Action_PassBlock` | RT | `16` | `15` | 65 | START | 65 | 134 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 65 | START | 77 | 82 |
| ✅ EXACT | `Action_PassBlock` | RG | `22` | `21` | 65 | START | 65 | 91 |
| ✅ EXACT | `Action_PassBlock` | LT | `4` | `3` | 65 | START | 65 | 117 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 76 | END | 62 | 76 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `10` | `9` | 78 | START | 78 | 103 |
| ✅ EXACT | `Action_BallCarry` | QB | `10` | `9` | 104 | START | 104 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 76 | 15 | inferred_complete_timeline |
| `Action_None` | 77 | 77 | 1 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 78 | 103 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 121 | 60 | inferred_complete_timeline |
| `Action_None` | 180 | 222 | 43 | inferred_complete_timeline |
| `Action_None` | 230 | 233 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 188 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 117 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 134 | 70 | inferred_complete_timeline |
| `Action_None` | 135 | 135 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 76 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 114 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 91 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 134 | 70 | inferred_complete_timeline |
| `Action_None` | 135 | 239 | 105 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 91 | 30 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 185 | 124 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 84 | 23 | inferred_complete_timeline |
| `Action_None` | 90 | 224 | 135 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 93 | 32 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 127 | 234 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 111 | 50 | inferred_complete_timeline |
| `Action_None` | 120 | 239 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 132 | 71 | inferred_complete_timeline |
| `Action_None` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 90–239 | 86 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 98–239 | 140 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 121–239 | 107 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 136–239 | 104 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 181–230 | 24 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 215–239 | 25 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [62–76], lower_priority='Action_PassBlock' annotated_start=65, effective_Action_PassBlock_start=77.
- ⚠️ Action 'Action_PassBlock' range [65-117] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-188] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 135, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [135-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-121] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-222] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-239] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-82] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-114] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-91] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-230] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>