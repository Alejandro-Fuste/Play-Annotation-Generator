# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_6`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Action 'Action_BallCarry' range [171-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-199] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [207-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-248] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [262-263] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-281] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-220] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-263] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-273] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-247] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [197-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-275] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [148-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [171-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-169] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-284] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-52] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-121] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-242] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-298] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-298] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-298] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-264] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-298] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-298] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.