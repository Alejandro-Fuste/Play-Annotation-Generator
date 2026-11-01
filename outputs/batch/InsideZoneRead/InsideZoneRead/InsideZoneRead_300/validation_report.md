# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_300`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_300/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [27–41], lower_priority='Action_ZoneBlock' annotated_start=30, effective_Action_ZoneBlock_start=42.
> - Action 'Action_None' range [27-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [67-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [197-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-39] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-99] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-90] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-62] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.