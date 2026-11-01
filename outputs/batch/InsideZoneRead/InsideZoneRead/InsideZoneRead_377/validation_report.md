# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_377`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_377/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [25–38], lower_priority='Action_ZoneBlock' annotated_start=28, effective_Action_ZoneBlock_start=39.
> - Action 'Action_None' range [25-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-109] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [63-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-44] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-103] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.