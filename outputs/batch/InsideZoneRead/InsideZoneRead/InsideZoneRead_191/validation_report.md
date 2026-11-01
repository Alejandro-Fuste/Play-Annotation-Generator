# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_191`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_191/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 29 |
| Ball Tracks | 2 |
| CSV events parsed | 20 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_ZoneBlock' annotated_start=20, effective_Action_ZoneBlock_start=31.
> - Action 'Action_ZoneBlock' range [20-43] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-71] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-43] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-112] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-35] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-146] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-72] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-50] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-96] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [51-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-180] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [19-37] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '30' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.