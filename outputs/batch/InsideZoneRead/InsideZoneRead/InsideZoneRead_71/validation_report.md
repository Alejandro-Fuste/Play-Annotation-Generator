# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_71`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [52–65], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=66.
> - Action 'Action_None' range [52-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-198] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-103] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-207] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-188] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-121] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-113] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [114-187] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-193] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.