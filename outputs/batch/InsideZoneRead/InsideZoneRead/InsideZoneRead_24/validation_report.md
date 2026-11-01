# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_24`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [26–38], lower_priority='Action_ZoneBlock' annotated_start=28, effective_Action_ZoneBlock_start=39.
> - Action 'Action_None' range [96-109] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-50] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-91] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-103] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '6' starts at frame 68, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [68-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-151] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-62] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [60-75] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-182] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-196] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '25' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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