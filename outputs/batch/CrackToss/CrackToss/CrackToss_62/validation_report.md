# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_62`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 399 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '24' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
> - Action 'Action_CrackBlock' range [307-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [326-364] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-399] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-388] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-399] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-347] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-380] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-315] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-379] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-395] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-303] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-322] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-379] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-395] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-379] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-381] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-399] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-377] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-395] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-328] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-379] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-385] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-394] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-397] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-378] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-398] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-383] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-395] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-356] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-372] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-379] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-386] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-303] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-367] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-376] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-376] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-392] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-363] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-381] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-339] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [340-369] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [373-374] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-399] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-379] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-396] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-368] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [370-371] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-399] for track '25' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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