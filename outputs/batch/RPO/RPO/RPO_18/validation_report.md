# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_18`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [43-57] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-85] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-128] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-91] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-88] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-199] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-58] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-117] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 98, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [98-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-60] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-123] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-156] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-153] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-173] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
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