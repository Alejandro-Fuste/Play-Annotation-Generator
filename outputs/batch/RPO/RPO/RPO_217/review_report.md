# Play-Annotation-Generator Annotation Review — RPO_217

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_217`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 120
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSeamRoute` | actor_track_id `2` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `6` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 63 | START | 63 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `14` | 63 | START | 63 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `18` | 63 | START | 63 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 63 | START | 63 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `3` | 63 | START | 63 | 98 |
| ✅ EXACT | `Action_ReadDefender` | QB | `12` | `12` | 74 | START | 74 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | QB | `12` | `12` | 83 | START | 83 | 84 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 115 | START | 115 | 118 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 73 | 12 | inferred_complete_timeline |
| `Action_ReadDefender` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_PullBall` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PullBall` | 86 | 94 | 9 | inferred_complete_timeline |
| `Action_None` | 95 | 114 | 20 | inferred_complete_timeline |
| `Action_ThrowPass` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 80 | 19 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 90 | 239 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `6`</summary>

- **xml_track_id:** `6`
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
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 90 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_None` | 84 | 216 | 133 | inferred_complete_timeline |
| `Action_None` | 218 | 231 | 14 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
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
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 98 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 118 | 16 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |
| `Action_None` | 150 | 167 | 18 | inferred_complete_timeline |
| `Action_None` | 169 | 187 | 19 | inferred_complete_timeline |
| `Action_None` | 189 | 209 | 21 | inferred_complete_timeline |
| `Action_None` | 221 | 239 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 118 | 56 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 126 | 239 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 125 | 239 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 79 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 88 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 88 | 27 | inferred_complete_timeline |
| `Action_None` | 93 | 112 | 20 | inferred_complete_timeline |
| `Action_None` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_None` | 138 | 154 | 17 | inferred_complete_timeline |
| `Action_None` | 160 | 169 | 10 | inferred_complete_timeline |
| `Action_None` | 189 | 215 | 27 | inferred_complete_timeline |
| `Action_None` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 143 | 82 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 153 | 215 | 63 | inferred_complete_timeline |
| `Action_None` | 218 | 230 | 13 | inferred_complete_timeline |
| `Action_None` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_None` | 85 | 239 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 100 | 39 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 122 | 218 | 97 | inferred_complete_timeline |
| `Action_None` | 220 | 239 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 123 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 77 | 16 | inferred_complete_timeline |
| `Action_None` | 86 | 91 | 6 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 239 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 191 | 130 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 103 | 42 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 239 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 18–66 | 48 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 76–239 | 136 | 10 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 87–239 | 153 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 100–132 | 33 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 118–152 | 23 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 129–239 | 110 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 142–239 | 92 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 166–239 | 59 | 6 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 171–181 | 5 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 178–239 | 22 | 5 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 223–235 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 93 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [62-191] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-103] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-98] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-118] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-187] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-209] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-88] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-112] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-154] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-239] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-143] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-230] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-100] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-239] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [83-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-231] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-121] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '19' starts at frame 63, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [63-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-106] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-151] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-132] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-138] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-239] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-219] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-184] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-235] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.

</details>