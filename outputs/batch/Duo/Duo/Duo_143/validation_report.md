# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_143`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_143/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 287: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-164] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-201] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-239] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-143] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-167] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-221] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-155] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-151] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-171] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [99-120] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-239] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '29' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.