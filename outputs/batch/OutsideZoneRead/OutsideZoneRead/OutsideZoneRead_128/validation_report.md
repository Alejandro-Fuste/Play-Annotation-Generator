# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_128`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [7–23], lower_priority='Action_ZoneBlock' annotated_start=10, effective_Action_ZoneBlock_start=24.
> - Action 'Action_None' range [7-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [10-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [34-44] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [54-276] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-276] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-282] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-21] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-298] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [10-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [10-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-98] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-88] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-282] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.