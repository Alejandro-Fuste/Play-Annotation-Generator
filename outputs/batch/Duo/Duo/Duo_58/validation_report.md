# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_58`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_PreSnap' range [0-319] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-354] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-336] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-347] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-358] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-327] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-286] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-358] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-356] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-358] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-316] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-334] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-338] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-354] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-322] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-358] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [270-274] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [279-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 306, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [306-306] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-332] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [270-274] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [279-287] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [296-305] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 306, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [306-306] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-341] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-287] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-250] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-30] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-323] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-346] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-240] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-248] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [270-283] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [286-305] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-358] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-315] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-340] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-344] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-355] for track '30' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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