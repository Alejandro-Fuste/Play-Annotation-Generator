# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_340`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_340/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [18–27], lower_priority='Action_ZoneBlock' annotated_start=21, effective_Action_ZoneBlock_start=28.
> - Action 'Action_None' range [18-38] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-47] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-34] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-76] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-62] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-151] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-37] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-113] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '10' starts at frame 28, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [28-28] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-67] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 18, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [18-18] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '12' starts at frame 21, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [21-47] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_Keep' range [37-62] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-63] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [55-85] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-116] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-180] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-167] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '34' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.