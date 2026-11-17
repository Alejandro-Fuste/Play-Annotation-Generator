# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_372`
- **Input XML**: `outputs/batch/Power/Power/Power_372/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [18-157] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-259] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-163] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-190] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-185] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [111-146] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-240] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-151] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [153-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-24] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-59] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-195] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-204] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-97] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-145] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-155] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-263] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-221] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-250] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-269] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-252] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-269] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.