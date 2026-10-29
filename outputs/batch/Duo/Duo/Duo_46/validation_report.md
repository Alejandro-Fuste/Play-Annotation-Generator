# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_46`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-232] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [138-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [161-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-196] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-219] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-233] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-191] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-239] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-155] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-166] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-177] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-178] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-239] for track '26' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.